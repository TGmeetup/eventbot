#!/usr/bin/env python3
# coding=utf-8

import io
import os
import subprocess

try:
    from .libs.EventIssueHandle import EventIssueHandle
    from .libs.LocalEventHandle import LocalEventHandle
except:
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
    issuehandle = EventIssueHandle("TGmeetup/TGevents")
    localhandle = LocalEventHandle("~/.config/TGmeetup/")

    issue_list = issuehandle.get_issue_list()
    localevent = localhandle.get_event_list()

    for i in localevent:
        # if i is in issue_list, update issue_list(remove i)
        # else
            # localhandle.get_event_detail(i)
            # issuehandle.add_issue(i)

    if len(issue_list) > 0:
        for i in issue_list:
            issuehandle.close_issue(i)


if __name__ == '__main__':
    main()
