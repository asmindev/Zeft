#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
            Author: zettamus || asmin
            Github: zettamus || asmin-dev
            From Xiuzcode
"""

from .feed import Comment, Other, React
from .get import user, Showgroup, Showalbum, Finduser
from .messages import Messages
from . import action
from . import group
from . import parsing
from . import friends
from . import images
#from .action import *
import re

class Account:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__username = None
        self.__profile_pic = None
        self.__login = False
    def GetMyInfo(self,ses):
        if "mbasic_logout_button" in str(ses.get("/me").content):
            self.__username = parsing.Urlfind(data, 'friends?lst').split('/')[1]
            photos = parsing.Parser(data).find_all("img")
            self.__name = parsing.Parser(data).find("title").text
            try:
                self.__id = re.findall('/(\d*)/allactivity',str(data))[0]
            except:
                pass
            for profile in photos:
                if "profile picture" in str(profile):
                    self.__profile_pic = profile["src"]
                    break
        return {
                "name"        :self.__name,
                "id"          :self.__id,
                "username"    :self.__username,
                "profile_pic" :self.__profile_pic
                }
    @property
    def logged(self):
        return self.__login
    def login(self,ses):
        self.__login = True if "mbasic_logout_button" in str(ses.get("/me").content) else False
        return self.__login
