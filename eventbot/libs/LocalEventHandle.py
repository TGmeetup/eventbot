#!/usr/bin/env python3
# coding=utf-8

import io
import os
import subprocess

class LocalEventHandle():
    def __init__(self, path):
        self.path = path

    def get_event_list(self):
        subprocess.check_output("grep name **/**/**/* | grep events.json", shell=True)
        pass

    def get_event_detail(self, event):
        pass

