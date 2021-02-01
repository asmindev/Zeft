#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zettamus || asmin

from .parser_html import Parsing
import re


def post(ses, target, query, nextstr, arg, amount):
    try:
        amount = int(amount)
        raw = Parsing(ses.get(target).content)
        for current in raw.find_url(query):
            arg.append(current.replace("https://m.facebook.com", ""))
            amount -= 1
            if amount == 0:
                return arg
        if nextstr in str(raw.to_bs4):
            post(ses, raw.find_url(nextstr), query, nextstr, arg, amount)
        return arg
    except Exception:
        return arg


def Showgroup(ses):
    current = []
    raw = Parsing(ses.get("/groups/?seemore").content)
    for group in raw.find_url("groups", True):
        if "category" in str(group["url"]) or "create" in str(group["url"]):
            continue
        current.append(
            dict(
                url=group["url"].split("com/")[1].replace("/?refid=27", ""),
                name=group["text"],
            )
        )
    return current


def Showalbum(ses, params):
    data = Parsing(ses.get(params + "/photos").content)
    if "albums/?owner_id" in str(data.to_bs4):
        album = data.find_url("album/?owner_id")
        albums = Parsing(album).find_url("albums", text=True)
    else:
        albums = data.find_url("/albums", text=True)
    return albums


def user(user):
    """
    Params must be str or bytes type

    """
    if "php?rand=" in str(user):
        raise ValueError("User not found ")
    return dict(
        name=re.findall("<title>(.*?)</title>", str(user))[0],
        id=re.findall("owner_id=(\d*)", str(user))[0],
    )


def Finduser(ses, name):
    return [
        {"name": user[1], "id": re.findall("id=(\d*)", str(user[0]))[0]}
        if "profile" in str(user[0])
        else {"name": user[1], "username": user[0].split("?")[0]}
        for user in re.findall(
            'profile picture".*?<a href="/(.*?)"><div class=".."><div.*?>(.*?)</div>',
            str(ses.get("search/people/?q=" + name).content),
        )
    ]
