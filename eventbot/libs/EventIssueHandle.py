#!/usr/bin/env python3
# coding=utf-8

import io
import os
import ast
import subprocess
import requests
import json
#import datetime
import markdown
from datetime import datetime, date
from bs4 import BeautifulSoup

class EventIssueHandle():
    def __init__(self, repo, authkey):
        self.repo = repo
        self.authkey = "token "+authkey
        self.github_api = "https://api.github.com/repos/"
        self.header = {'Content-type': 'application/vnd.github.symmetra-preview+json;', 'Authorization': self.authkey}

    def get_issue_list(self, label):
        # Get issues from GitHub, and return list
        all_event_issue = []
        url = self.github_api+self.repo+"/issues"
        result = requests.get(url, headers=self.header)
        events_info = result.json()
        for e in events_info:
            if e["state"] == "open":
                for l in e["labels"]:
                    if l["name"] == label:
                        soup = BeautifulSoup(e["body"], "html.parser")
                        try:
                            body = json.loads(soup.details.string)
                        except:
                            body = ast.literal_eval(soup.details.string)
                        all_event_issue.append({
                            "title": e["title"],
                            "id": e["id"],
                            "number": e["number"],
                            "datetime": body["datetime"],
                            "name": body["name"],
                            "groupRef": body["groupRef"]
                        })
        return all_event_issue

    def close_issue(self, num):
        # Remove issue from GitHub by issue num
        url = self.github_api+self.repo+"/issues/"+str(num)
        result = requests.patch(url, data='{"state": "close", "labels":[]}', headers=self.header)

    def generate_issue(self, data, groupRef):
        eventdate = datetime(int(data["local_date"].split("-")[0]),
                          int(data["local_date"].split("-")[1]),
                          int(data["local_date"].split("-")[2]),
                          int(data["local_time"].split(":")[0]),
                          int(data["local_time"].split(":")[1]))
        try:
            detaildata = [{
                "name": data["name"],
                "datetime": data["local_date"]+"T"+data["local_time"]+":00.000Z",
                "local_city": data["local_city"],
                "location": data["location"],
                "geocode": data["geocode"],
                "geocodeFromGroup": data["geocodeFromGroup"],
                "link": data["link"],
                "groupRef": groupRef
            }]
        except:
            detaildata = [{
                "name": data["name"],
                "datetime": data["local_date"]+"T"+data["local_time"]+":00.000Z",
                "local_city": data["local_city"],
                "location": " ",
                "geocode": data["geocode"],
                "geocodeFromGroup": data["geocodeFromGroup"],
                "link": data["link"],
                "groupRef": groupRef
            }]
        body = "<h1> "+data["name"]+"</h1>  \
                <h3> ● 報名連結 / Registration link </h3> <a href='"+data["link"]+"'>"+data["link"]+"</a>  <br> \
                <h3> ● 地點 / Location</h3>   "+detaildata[0]["location"] +" @ "+data["local_city"]+"  <br> \
                <h3> ● 時間 / Date Time</h3>  "+eventdate.strftime("%A, %d. %B %Y %H:%M")+" :clock7:  <br> \
                <h3> ● 主辦單位資訊 / Group Information   </h3>\
                - Category: "+groupRef.split('/')[0]+" <br>  \
                - Name: "+groupRef.split('/')[2]+"  <br> \
                - URL: <a href='https://raw.githubusercontent.com/TGmeetup/TGmeetup/master/"+groupRef+"/README.md'>https://raw.githubusercontent.com/TGmeetup/TGmeetup/master/"+groupRef+"/README.md</a>   <br> \
                <br><hr/><br> \
                <blockquote><p> Pure data is right below <br> \
                Leave it!</p></blockquote> \
                <details>"+str(detaildata[0])+"</detail>"
        return body

    def add_issue(self, data, groupRef):
        body = self.generate_issue(data, groupRef)
        url = self.github_api+self.repo+"/issues"
        eventdate = date(int(data["local_date"].split("-")[0]),
                          int(data["local_date"].split("-")[1]),
                          int(data["local_date"].split("-")[2]))
        payload ="{\
              \"title\": \"【"+eventdate.strftime("%B %d")+"】"+data["name"]+"\",\
              \"body\": \""+str(body)+"\",\
              \"state\": \"open\",\
              \"labels\": [\
                \"Event\"\
              ]}"
        pprint(payload)
        result = requests.post(url, headers=self.header, data=payload.encode('utf-8'))
        print(result)
