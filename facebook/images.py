#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zett | Asmin
from .parser_html import Parsing


def getimage(requests, link, nextstr, args=[]):
    data = Parsing(requests.get(link).content)
    linked = data.find_url("preview")
    if type(linked) != list:
        args.append(linked)
    else:
        [args.append(image) for image in linked]
    if nextstr in str(data.to_bs4):
        getimage(requests, data.find_url(nextstr), nextstr, args)
    list_img = []
    for photos in args:
        img = Parsing(requests.get(photos).content).find_url("fupg")
        list_img.append(img)
    return list_img


def fullsize(ses, args):
    arg = []
    for photos in args:
        link_to_full_size = Parsing(ses.get(photos).content).find_url("full")
        full_size = Parsing(ses.get(link_to_full_size).content).find_url('fupg')
        if len(full_size) != 0:
            arg.append(full_size)
    return arg


def inbox(ses, area):
    url = Parsing(ses.get(area).content).find_url("thread")
    return getimage(ses, url, "pagination_direction=")


def album(ses, link, args=[]):
    raw = Parsing(ses.get(link).content)
    for photos in raw.find_url("photo.php"):
        args.append(photos)
    if "?start" in str(raw.to_bs4):
        album(ses, raw.find_url("?start"), args)
    return fullsize(ses, args)
