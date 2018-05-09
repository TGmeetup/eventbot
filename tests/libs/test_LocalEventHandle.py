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

from eventbot.libs.LocalEventHandle import LocalEventHandle

class TestGetEventFiles:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        file_list = localhandle.get_event_files()
        assert file_list == ['tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json']

class TestGetEventList:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        events_list = localhandle.get_event_list()
        assert events_list == [{'path': 'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json', 'groupRef': 'community/tw/DevOpsTaiwan', 'name': 'SRE 讀書會 #7', 'datetime': '2018-02-08T19:30:00:00.000Z', 'event_num': 0}]
