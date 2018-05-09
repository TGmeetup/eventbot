#!/usr/bin/env python3
# coding=utf-8

import io
import os
import subprocess
import requests
import json
from bs4 import BeautifulSoup

class EventIssueHandle():
    def __init__(self, repo):
        self.repo = repo
        self.github_api = "https://api.github.com/repos/"

    def get_issue_list(self):
        # Get issues from GitHub, and return list
        all_event_issue = []
        header = {'Content-type': 'application/vnd.github.symmetra-preview+json'}
        url = self.github_api+self.repo+"/issues"
        result = requests.get(url, headers=header)
        events_info = result.json()
        print(events_info)
        for e in events_info:
            if e["state"] == "open":
                for l in e["labels"]:
                    if l["name"] == "Event":
                        soup = BeautifulSoup(e["body"], "html.parser")
                        body = json.loads(soup.details.string)
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
        pass

    def add_issue(self, event):
        pass

#def main():
#    issuehandle = EventIssueHandle("TGmeetup/TGevents")
#    issuehandle.get_issue_list()

#if __name__ == '__main__':
#    main()
