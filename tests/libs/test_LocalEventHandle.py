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
            'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json',
            'tests/test_data/TGmeetup/community/tw/DigitalOceanHsinchu/events.json']


class TestGetEventList:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        events_list = localhandle.get_event_list()
        print(events_list)
        assert events_list == [
            {
                'path': 'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json',
                'groupRef': 'community/tw/DevOpsTaiwan',
                'name': 'DevOps Taiwan - Monitoring Tools 大亂鬥',
                'datetime': '2018-05-26T14:00:00.000',
                'event_num': 0},
            {
                'path': 'tests/test_data/TGmeetup/community/tw/DigitalOceanHsinchu/events.json',
                'groupRef': 'community/tw/DigitalOceanHsinchu',
                'name': 'Ansible with DigitalOcean',
                'datetime': '2018-05-14T18:50:00.000',
                'event_num': 0}]


class TestGetEventDetail:
    def test_normal(self):
        localhandle = LocalEventHandle("tests/test_data/TGmeetup")
        event = localhandle.get_event_detail(
            {
                'path': 'tests/test_data/TGmeetup/community/tw/DevOpsTaiwan/events.json',
                'groupRef': 'community/tw/DevOpsTaiwan',
                'name': 'DevOps Taiwan - Monitoring Tools 大亂鬥',
                'datetime': '2018-05-26T14:00:00.000',
                'event_num': 0})
        assert event == {
            "geocode": {
                "lat": 25.0329694,
                "lng": 121.5654177
            },
            "geocodeFromGroup": "true",
            "link": "https://devops.kktix.cc/events/monitoring-tools",
            "local_city": "Taipei",
            "local_date": "2018-05-26",
            "local_time": "14:00:00",
            "name": "DevOps Taiwan - Monitoring Tools 大亂鬥"}
