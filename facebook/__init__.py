#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
            Author: zettamus || asmin
            Github: zettamus || asmin-dev
            From Xiuzcode
"""

# from .action import *
import re

from . import action, friends, group, images, parsing
from .feed import Comment, Other, React
from .get import Finduser, Showalbum, Showgroup, user
from .messages import Messages
from .parser_html import Parsing

__VERSION__ = "0.1"


class Account:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__username = None
        self.__profile_pic = None
        self.__login = False

    def getMyInfo(self, ses, data=None):
        if "mbasic_logout_button" in str(data.to_bs4):
            try:
                self.__username = data.find_url("friends?lst").split("/")[1]
            except Exception:
                pass
            # Disabled
            # self.__profile_pic = parsing.Urlfind(Parser(ses.get(parsing.Urlfind(Parser(ses.get(parsing.Urlfind(data, "photo.php?fbid")).content), 'full_size')).content),'fupg')
            self.__name = data.to_bs4.find("title").text
            try:
                self.__id = re.findall(
                    "/(\d*)/allactivity", str(data.to_bs4))[0]
            except Exception:
                pass
        return {
            "name": self.__name,
            "id": self.__id,
            "username": self.__username,
            "profile_pic": self.__profile_pic,
        }

    @property
    def logged(self):
        return self.__login

    def login(self, ses):
        data = Parsing(ses.get("profile.php").content)
        if "mbasic_logout_button" in str(data.to_bs4):
            self.__login = self.getMyInfo(ses, data)
        else:
            data = Parsing(
                ses.get(
                    "mobile/zero/carrier_page/feature_switch/?feature_is_on=1&carrier_page_enabled=0",
                    host="https://free.facebook.com",
                ).content
            )
            if "signup_button_area" not in str(data.to_bs4):
                form = data.parsing_form("carrier_page")
                act = form["action"]
                form.pop("action")
                data = ses.post(
                    act, form, host="https://free.facebook.com").content
                data = Parsing(ses.get("profile.php").content)
                if "mbasic_logout_button" in str(data.to_bs4):
                    self.__login = self.getMyInfo(ses, data)

        return self.__login
