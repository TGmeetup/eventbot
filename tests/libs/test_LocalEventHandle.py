#!/usr/bin/env python3
# coding=utf-8
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

from eventbot.libs.LocalEventHandle import LocalEventHandle


class TestGetEventFiles:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        file_list = localhandle.get_event_files()
        assert file_list == [
            'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json']


class TestGetEventList:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        events_list = localhandle.get_event_list()
        assert events_list == [
            {
                'path': 'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json',
                'groupRef': 'community/tw/DevOpsTaiwan',
                'name': 'SRE 讀書會 #7',
                'datetime': '2018-02-08T19:30:00:00.000Z',
                'event_num': 0}]


class TestGetEventDetail:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        event = localhandle.get_event_detail(
            {
                'path': 'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json',
                'groupRef': 'community/tw/DevOpsTaiwan',
                'name': 'SRE 讀書會 #7',
                'datetime': '2018-02-08T19:30:00:00.000Z',
                'event_num': 0})
        assert event == {
            'geocode': {
                'lat': 25.0329694,
                'lng': 121.5654177},
            'geocodeFromGroup': 'true',
            'link': 'https://devops.kktix.cc/events/sre-7',
            'local_city': 'Taipei',
            'local_date': '2018-02-08',
            'local_time': '19:30:00',
            'name': 'SRE 讀書會 #7'}
