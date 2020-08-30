#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zettamus || asmin

from .parsing import Parser, Urlfind
import re
def post(ses, target,query, nextstr, arg, amount):
    try:
        amount = int(amount)
        raw = Parser(ses.get(target).content)
        for current in Urlfind(raw,query):
            arg.append(current)
            amount -= 1
            if amount == 0:
                return arg
        if nextstr in str(raw):
            post(ses, Urlfind(raw, nextstr), query, nextstr, arg, amount)
        return arg
    except:
        return arg

def Showgroup(ses):
        current = []
        raw = Parser(ses.get('/groups/?seemore').content)
        for group in Urlfind(raw,'groups',True):
            if 'category' in str (group["url"]) or 'create' in str(group["url"]):
                continue
            current.append({
                'url' : group["url"].replace('?refid=27',''),
                "name" :group["text"]
                })
        return current
def Showalbum(ses, params):
    data = Parser(ses.get(params + '/photos').content)
    return Urlfind(Parser(ses.get(Urlfind(data,'albums/?owner_id')).content),'/albums',text=True) if 'albums/?owner_id' in str(data) else Urlfind(data, '/albums', text=True)
def user(user):
    """
    Params must be str or bytes type

    """
    if 'php?rand=' in str(user):
        raise ValueError('User not found ')
    return {
            'name' :re.findall('<title>(.*?)</title>',str(user))[0],
            'id'   :re.findall('owner_id=(\d*)',str(user))[0]
            }
def Finduser(ses, name):
    return [{"name": user[1], "id": re.findall('id=(\d*)',str(user[0]))[0]} if "profile" in str(user[0]) else {"name": user[1], "username": user[0].split("?")[0]} for user in re.findall('profile picture".*?<a href="/(.*?)"><div class=".."><div.*?>(.*?)</div>',str(ses.get('search/people/?q=' + name).content))]
