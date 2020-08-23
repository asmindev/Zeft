#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zettamus | asmin 
"""
:Parsing response to many function

"""
import re
from bs4 import BeautifulSoup

def Parser(raw):
    """
    Change type response to bs4

    """
    return BeautifulSoup(raw,"html.parser")
def Urlfind(raw, string, text = False, **args):
    lisT = []
    for url in raw.find_all("a", args, href=True):
        if 'zero/toggle' in str(url["href"]) or 'upsell' in str(url['href']):
            continue
        if text:
            if string in str(url):
                lisT.append(
                    {
                        'url'  :url["href"],
                        'text' :url.text
                        }
                    )
        else:
            if string in str(url):
                lisT.append(url['href'])
    return lisT[0] if len(lisT) == 1 else lisT
def form(raw, string):
    """
    Get form input value with specified action url
    """
    rv = {}
    for x in Parser(raw).find_all('form'):
        if string in str(x['action']):
            rv["action"] = x["action"]
            for i in x.find_all('input'):
                try:
                    rv[i["name"]] = i["value"]
                except: continue
    return rv

