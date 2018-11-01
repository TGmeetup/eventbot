#!/usr/bin/env python3
# coding=utf-8

import requests
import json
from datetime import datetime, date, timezone, timedelta
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote


class EventIssueHandle():
    def __init__(self, repo, authkey):
        self.repo = repo
        self.authkey = "token " + authkey
        self.github_api = "https://api.github.com/repos/"
        self.header = {
            'Content-type': 'application/vnd.github.symmetra-preview+json;',
            'Authorization': self.authkey}

    def get_issue(self, title, label):
        url = "https://api.github.com/search/issues?q=label:" + label + \
            "+state:open+repo:" + self.repo + "+state:open+in:" + title
        result = requests.get(url, headers=self.header)
        event_info = result.json()
        if event_info.items != []:
            return True
        else:
            return False

    def get_issue_list(self, label):
        # Get issues from GitHub, and return list
        all_event_issue = []
        url = self.github_api + self.repo + "/issues"
        result = requests.get(url, headers=self.header)
        events_info = result.json()
        for e in events_info:
            if e["state"] == "open":
                for l in e["labels"]:
                    if l["name"] == label:
                        soup = BeautifulSoup(e["body"], "html.parser")
                        body = json.loads(unquote(soup.details.string))
                        event_time = datetime.strptime(
                            body["datetime"][:-10], '%Y-%m-%dT%H:%M:%S')
                        event_time = event_time.astimezone(
                            timezone(
                                timedelta(
                                    hours=16))).isoformat(
                            timespec='milliseconds')
                        all_event_issue.append({
                            "title": e["title"],
                            "id": e["id"],
                            "number": e["number"],
                            "datetime": event_time[:-6],
                            "name": body["name"],
                            "group_ref": body["group_ref"]
                        })
        return all_event_issue

    def close_issue(self, num):
        # Remove issue from GitHub by issue num
        url = self.github_api + self.repo + "/issues/" + str(num)
        requests.patch(
            url,
            data='{"state": "close", "labels":[]}',
            headers=self.header)

    def taipei_to_utc_time(self, local_date, local_time):
        eventdate = datetime(int(local_date.split("-")[0]),
                             int(local_date.split("-")[1]),
                             int(local_date.split("-")[2]),
                             int(local_time.split(":")[0]),
                             int(local_time.split(":")[1]))
        utc_eventdate = eventdate.astimezone(
            timezone(
                offset=timedelta(
                    hours=0))).isoformat(
            timespec='milliseconds')
        return eventdate, utc_eventdate

    def generate_issue(self, data, group_ref):
        eventdate, utc_eventdate = self.taipei_to_utc_time(
            data["local_date"], data["local_time"])
        try:
            detaildata = [{
                "name": data["name"],
                "datetime": str(utc_eventdate),
                "local_city": data["local_city"],
                "location": data["location"],
                "geocode": data["geocode"],
                "geocodeFromGroup": data["geocodeFromGroup"],
                "link": data["link"],
                "group_ref": group_ref
            }]
        except BaseException:
            detaildata = [{
                "name": data["name"],
                "datetime": str(utc_eventdate),
                "local_city": data["local_city"],
                "location": "",
                "geocode": data["geocode"],
                "geocodeFromGroup": data["geocodeFromGroup"],
                "link": data["link"],
                "group_ref": group_ref
            }]
        print(data["name"])
        body = "<h1> " + data["name"] + "</h1>  \
                <h3> ● 報名連結 / Registration link </h3> <a href='" + data["link"] + "'>" + data["link"] + "</a>  <br> \
                <h3> ● 地點 / Location</h3>   " + detaildata[0]["location"] + " @ " + data["local_city"] + "  <br> \
                <h3> ● 時間 / Date Time</h3>  " + eventdate.strftime("%A, %d. %B %Y %H:%M") + " :clock7:  <br> \
                <h3> ● 主辦單位資訊 / Group Information   </h3>\
                - Category: " + group_ref.split('/')[0] + " <br>  \
                - Name: " + group_ref.split('/')[2] + "  <br> \
                - URL: <a href='https://raw.githubusercontent.com/TGmeetup/TGmeetup/master/" + group_ref + "/README.md'>https://raw.githubusercontent.com/TGmeetup/TGmeetup/master/" + group_ref + "/README.md</a>   <br> \
                <br><hr/><br> \
                <blockquote><p> Pure data is right below <br> \
                Leave it!</p></blockquote> \
                <details>" + quote(json.dumps(detaildata[0])) + "</detail>"
        return body

    def add_issue(self, data, group_ref):
        body = self.generate_issue(data, group_ref)
        url = self.github_api + self.repo + "/issues"
        eventdate = date(int(data["local_date"].split("-")[0]),
                         int(data["local_date"].split("-")[1]),
                         int(data["local_date"].split("-")[2]))
        payload = "{\
              \"title\": \"【" + eventdate.strftime("%B %d") + "】《" + group_ref.split('/')[2] + "》" + data["name"] + "\",\
              \"body\": \"" + str(body) + "\",\
              \"state\": \"open\",\
              \"labels\": [\
                \"Event\"\
              ]}"
        # pprint(payload)
        result = requests.post(url, headers=self.header, data=payload.encode('utf-8'))
        print(result)
