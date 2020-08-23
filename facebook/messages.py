#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zettamus || asmin
# github: asmin-dev?
from .parsing import form, Parser, Urlfind 
from concurrent.futures import ThreadPoolExecutor
class Messages:
    def __init__(self):
        self.__group = 'messages/read?tid=cid.g.'
        self.__people = 'messages/read?tid=cid.c.'
    def getForm(self, ses, type):
        return form(ses.get(type).content, 'send')
    def people(self, ses, user, msg, amount=1):
        farm = self.getForm(ses, self.__people + user)
        farm["ids["+user+"]"] = user
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
            del farm["like"], farm["send_photo"], farm["action"]
        except:
            raise ValueError('Invalid ID')
        for _ in range(amount):
            ses.post(ses, url, farm)
    def getmsg(self, ses):
        return get(ses, [],'messages',1)
    def delete_msg(self, ses, link):
        forms = form(ses.get(link).content,'action_redirect')
        action = forms["action"]
        fbjoe = dict(fb_dtsg=forms["fb_dtsg"],jazoest=forms["jazoest"],delete=forms["delete"])
        ses.get(Urlfind(Parser(ses.post(action, fbjoe).content),'?mm_action'))
    def getusersonline(self, ses):
        rv = []
        data = Parser(ses.get('buddylist.php').content).find_all('tr')
        for x in data:
            try:
                if "jY8pG8.png" in x.find('img')["src"]:
                    url = x.find('a')["href"]
                    if 'php' in str(url):
                        continue
                    else:
                        rv.append(url.split('id=')[1].split('&')[0])
            except:
                continue
        return rv
def get(ses, arg, url, page):
    raw = Parser(ses.get(url).content)
    for msg in Urlfind(raw, '?tid=', True):
        arg.append(msg)
    if 'see_older_threads' in str(raw):
        nextpage = Urlfind(raw, '?pageNum=' + str(page))
        page += 1
        get(ses, arg, nextpage, page)
    return arg
