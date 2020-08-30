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
from .parsing import Parser

__VERSION__ = "0.1"


class Account:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__username = None
        self.__profile_pic = None
        self.__login = False

    def __GetMyInfo(self, data=None):
        if "mbasic_logout_button" in str(data):
            self.__username = parsing.Urlfind(data, "friends?lst").split("/")[1]
            photos = data.find_all("img")
            self.__name = data.find("title").text
            try:
                self.__id = re.findall("/(\d*)/allactivity", str(data))[0]
            except:
                pass
            for profile in photos:
                if "profile picture" in str(profile):
                    self.__profile_pic = profile["src"]
                    break
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
        data = ses.get("me").content
        self.__login = (self.__GetMyInfo(Parser(data))if "mbasic_logout_button" in str(data) else False)

        return self.__login
