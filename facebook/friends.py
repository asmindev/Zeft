#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: asmin
from .parsing import Urlfind, Parser, form


def confirm(ses):
    return function(ses, "friends/center/requests", "confirm")


def delete(ses):
    return function(ses, "friends/center/requests", "delete", [])


def cancel(ses):
    return function(ses, "friends/center/requests/outgoing", "cancel", [])


def unfriend(ses):
    return [
        form(
            ses.get(Urlfind(Parser(ses.get(user).content), "removefriend")).content,
            "remove",
        )
        for user in getFl(ses, "me/friends", [])
    ]


def function(ses, url, type, args):
    frx = Parser(ses.get(url).content)
    raw = Urlfind(frx, type)
    for user in raw:
        args.append(user)
    if "ppk=" in str(frx):
        function(ses, Urlfind(frx, "ppk="), type, args)
    return args


def getFl(ses, url, args):
    frx = Parser(ses.get(url).content)
    for teman in Urlfind(frx, "?fref"):
        args.append(teman.split("?")[0])
    if "?unit" in str(frx):
        getFl(ses, Urlfind(frx, "?unit"), args)
    return args
