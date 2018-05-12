# !/usr/bin/env python3
# coding=utf-8
import configparser

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

from eventbot.libs.EventIssueHandle import EventIssueHandle


class TestGetIssueList:
    def test_normal(self):
        config = configparser.ConfigParser()
        config.read("AuthKey.cfg")
        issuehandle = EventIssueHandle(
            "TGmeetup/TGevents",
            config['GitHub_kay']['API_KEY'])
        issue_list = issuehandle.get_issue_list("code_test")
        assert issue_list[0]["title"] == "【May 9】For test case"
        assert issue_list[0]["id"] == 321417295
        assert issue_list[0]["number"] == 4
        assert issue_list[0]["name"] == "For test case"
        assert issue_list[0]["groupRef"] == "community/tw/DigitalOceanHsinchu"


class TestIssues:
    def test_normal(self):
        # issuehandle = EventIssueHandle("TGmeetup/TGevents")
        # issuehandle.add_issue({'geocode': {'lat': 25.0329694, 'lng': 121.5654177}, \
        # 'geocodeFromGroup': 'true', \
        # 'link': 'https://devops.kktix.cc/events/monitoring-tools', \
        # 'local_city': 'Taipei', 'local_date': '2018-05-26', 'local_time': '14:00:00',\
        # 'name': 'DevOps Taiwan - Monitoring Tools 大亂鬥'}, "community/tw/PyHUG")
        # issuehandle.close_issue(6)
        pass
