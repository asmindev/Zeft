#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: asmin
from .parser_html import Parsing


def confirm(ses):
    return function(ses, "friends/center/requests", "confirm")


def delete(ses):
    return function(ses, "friends/center/requests", "delete", [])


def cancel(ses):
    return function(ses, "friends/center/requests/outgoing", "cancel", [])


def unfriend(ses):
    data = []
    for user in getFl(ses, "me/friends", []):
        friend = Parsing(ses.get(user).content).find_url("removefriend")
        _data = Parsing(ses.get(friend).content).find_url("remove")
        data.append(_data)


def function(ses, url, type, args):
    frx = Parsing(ses.get(url).content)
    raw = frx.find_url(type)
    for user in raw:
        args.append(user)
    if "ppk=" in str(frx.to_bs4):
        function(ses, frx.find_url("ppk="), type, args)
    return args


def getFl(ses, url, args):
    frx = Parsing(ses.get(url).content)
    for teman in frx.find_url("?fref"):
        args.append(teman.split("?")[0])
    if "?unit" in str(frx.to_bs4):
        getFl(ses, frx.find_url("?unit"), args)
    return args
