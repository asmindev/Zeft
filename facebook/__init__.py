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

    def getMyInfo(self, ses, data=None):
        if "mbasic_logout_button" in str(data):
            try:
                self.__username = parsing.Urlfind(data, "friends?lst").split("/")[1]
            except:
                self.__username = None
            # Disabled
            #self.__profile_pic = parsing.Urlfind(Parser(ses.get(parsing.Urlfind(Parser(ses.get(parsing.Urlfind(data, "photo.php?fbid")).content), 'full_size')).content),'fupg')
            self.__name = data.find("title").text
            try:
                self.__id = re.findall("/(\d*)/allactivity", str(data))[0]
            except:
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
        data = ses.get("profile.php").content
        self.__login = (self.getMyInfo(ses, Parser(data)) if "mbasic_logout_button" in str(data) else False)

        return self.__login
