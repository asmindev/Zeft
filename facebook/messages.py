#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zettamus || asmin
# github: asmin-dev?
from .parser_html import Parsing


class Messages:
    def __init__(self):
        self.__group = "messages/read?tid=cid.g."
        self.__people = "messages/read?tid=cid.c."

    def getForm(self, ses, type):
        return Parsing(ses.get(type).content).parsing_form("send")

    def people(self, ses, user, msg, amount=1):
        farm = self.getForm(ses, self.__people + user)
        farm["ids[" + user + "]"] = user
        farm["body"] = msg
        url = farm["action"]
        del farm["action"]
        for x in range(amount):
            ses.post(url, farm)

    def group(self, ses, user, msg, amount):
        farm = self.getForm(ses, self.__group + user)
        farm["body"] = msg
        url = farm["action"]
        try:
            del farm["like"]
            del farm["send_photo"]
            del farm["action"]
        except Exception:
            raise ValueError("Invalid ID")
        for _ in range(amount):
            ses.post(ses, url, farm)

    def getmsg(self, ses):
        return get(ses, [], "messages", 1)

    def delete_msg(self, ses, link):
        forms = Parsing(ses.get(link).content).find_url("action_redirect")
        action = forms["action"]
        fbjoe = dict(
            fb_dtsg=forms["fb_dtsg"],
            jazoest=forms["jazoest"],
            delete=forms["delete"]
        )
        ses.get(Parsing(ses.post(action, fbjoe).content).find_url("?mm_action"))

    def getusersonline(self, ses):
        rv = []
        data = Parsing(ses.get("buddylist.php").content).to_bs4.find_all("tr")
        for x in data:
            try:
                if "jY8pG8.png" in x.find("img")["src"]:
                    url = x.find("a")["href"]
                    if "php" in str(url):
                        continue
                    else:
                        rv.append(url.split("id=")[1].split("&")[0])
            except Exception:
                continue
        return rv


def get(ses, arg, url, page):
    raw = Parsing(ses.get(url).content)
    for msg in raw.find_url("?tid=", text=True):
        arg.append(msg)
    if "see_older_threads" in str(raw.to_bs4):
        nextpage = raw.find_url("?pageNum=" + str(page))
        page += 1
        get(ses, arg, nextpage, page)
    return arg
