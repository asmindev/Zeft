#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zett | Asmin
from .get import user
from .parsing import Parser, Urlfind


def getimage(requests, link, nextstr, args=[]):
    data = Parser(requests.get(link).content)
    linked = Urlfind(data, "preview")
    if type(linked) != list:
        args.append(linked)
    else:
        [args.append(image) for image in linked]
    if nextstr in str(data):
        getimage(requests, Urlfind(data, nextstr), nextstr, args)
    listl = []
    [
        listl.append(Urlfind(Parser(requests.get(photos).content), "fupg"))
        for photos in args
    ]
    return listl


def fullsize(ses, args):
    arg = []
    for photos in args:
        data = Urlfind(
            Parser(ses.get(Urlfind(Parser(ses.get(photos).content), "full")).content),
            "fupg",
        )
        if len(data) != 0:
            arg.append(data)
    return arg


def inbox(ses, user):
    url = Urlfind(Parser(ses.get(user).content), "thread")
    return getimage(ses, url, "pagination_direction=")


def album(ses, link, args=[]):
    raw = Parser(ses.get(link).content)
    for photos in Urlfind(raw, "photo.php"):
        args.append(photos)
    if "?start" in str(raw):
        album(ses, Urlfind(raw, "?start"), args)
    return fullsize(ses, args)
