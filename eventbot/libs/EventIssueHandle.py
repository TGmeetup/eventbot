#!/usr/bin/env python3
# coding=utf-8

import io
import os
import subprocess

class EventIssueHandle():
    def __init__(self, repo):
        self.repo = repo

    def get_issue_list(self):
        # Get issues from GitHub, and return list
        pass

    def close_issue(self, num):
        # Remove issue from GitHub by issue num
        pass

    def add_issue(self, event):
        pass
