# !/usr/bin/env python3
# coding=utf-8

import subprocess
import configparser
from datetime import datetime
try:
    from .libs.EventIssueHandle import EventIssueHandle
    from .libs.LocalEventHandle import LocalEventHandle
except BaseException:
    from libs.EventIssueHandle import EventIssueHandle
    from libs.LocalEventHandle import LocalEventHandle

"""
Code flow:
1. tgmeetup -u
2. Get all issues list
3. Check there is the same issue
    - if yes, remove the item from issues list
    - if no, cp event.json -> create issue
      remove the item from issues list
      add tag
4. if there is an item in issues list, close the issue from GitHub
"""


def main():
    subprocess.check_output("tgmeetup -u", shell=True)

    config = configparser.ConfigParser()
    config.read("AuthKey.cfg")
    issuehandle = EventIssueHandle(
        "TGmeetup/TGmeetup.github.io",
        config['GitHub_kay']['API_KEY'])
    localhandle = LocalEventHandle("~/.config/TGmeetup")

    issuelist = issuehandle.get_issue_list("Event")
    issue_list = issuelist
    localevent = localhandle.get_event_list()

    if len(issuelist) == 0:
        for i in localevent:
            detail_event = localhandle.get_event_detail(i)
            issuehandle.add_issue(detail_event, i["group_ref"])

    if len(issuelist) != 0:
        for i in localevent:
            add_event = True
            for j in issuelist:
                # If local event is on GitHub issue, remove the adding event list from
                # memory
                if j["name"] == i["name"] and j["datetime"] == i["datetime"]:
                    issue_list.remove(j)
                    add_event = False
            # If local event is not on GitHub issue, search again
            # If found the local event is on GitHub, add_event is False
            if issuehandle.get_issue(i["name"], "Event") is True:
                add_event = False
            else:
                add_event = True
            # Finally, if add_event is True, let's add this local event on GitHub issue
            if add_event is True:
                detail_event = localhandle.get_event_detail(i)
                issuehandle.add_issue(detail_event, i["group_ref"])

    # Close the GitHub issue which need to close from memory(30)
    if len(issue_list) > 0:
        for i in issue_list:
            if datetime.strptime(i["datetime"].split("T")[0],
                                 '%Y-%m-%d') < datetime.now():
                issuehandle.close_issue(i["number"])
    # Search GitHub issue by title < Today and close these GitHub issue
    # Todo..


if __name__ == '__main__':
    main()
