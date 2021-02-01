#!/usr/bin/env python3
# -*-  coding: utf-8 -*-
# author: asmin | zettamus
import requests


def download(items):
    return requests.get(items).content
