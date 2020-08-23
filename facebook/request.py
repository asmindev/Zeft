#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# author: zettamus
# github: zettamus

import requests
class Browser:
    def __init__(self):
        self.__req = requests.get
        self.__post = requests.post
        self.__cookies = {"cookie": None}
        self.__host = "https://mbasic.facebook.com"
    @property
    def cookies(self):
        pass
    @cookies.setter
    def setkuki(self, kuki):
        self.__cookies = {"cookie": kuki}
    @cookies.getter
    def showkuki(self):
        return self.__cookies
    def get(self,url):
        try:
            if self.__cookies["cookie"] == None:
                raise ValueError("Please set your cookie!")
            return self.__req(self.__host + check(url), cookies = self.__cookies)
        except requests.exceptions.ConnectionError as f:
            raise ConnectionError(str(f))
    def post(self, url, data):
        try:
            if self.__cookies["cookie"] == None:
                raise ValueError("Please set your cookie!")
            return self.__post(self.__host + check(url), data = data, cookies = self.__cookies)
        except requests.exceptions.ConnectionError as f:
            raise ConnectionError(str(f))
def check(url):
    try:
        return url if url.startswith('/') else '/' + url
    except AttributeError as f:
        raise ValueError(f'Invalid url {str(f)}')




