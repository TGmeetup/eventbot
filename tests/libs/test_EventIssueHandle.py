#!/usr/bin/env python3
# coding=utf-8
import json
import pytest
import subprocess
import os
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

from eventbot.libs.EventIssueHandle import EventIssueHandle

class TestGetIssueList:
    def test_normal(self):
        issuehandle = EventIssueHandle("TGmeetup/TGevents")
        issue_list = issuehandle.get_issue_list("code_test")
        assert issue_list == [{'title': '【May 9】For test case', 'id': 321417295, 'number': 4, 'datetime': '2018-05-09T11:00:00.000Z', 'name': 'For test case', 'groupRef': 'community/tw/PyHUG'}]
