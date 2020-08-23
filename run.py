#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Coded by zettamus
# Github : zettamus
# Facebook : fb .me/zettid.1 
# Telegram : t.me/zettamus
# if you want to recode please dont change name author
# +---------------------------------+

R = '\033[31;m'
C = '\033[36;m'
G = '\033[35;m'
B = '\033[94;m'
r = '\033[0;m'
import os
import re
import sys
import time 
import cursor
import shutil
import random
import facebook
from getpass import getpass
from facebook.request import Browser
from threading import Thread
from colorama import Fore, Back, init
from concurrent.futures import ThreadPoolExecutor
init(True)
# var global
STATUS = None
penentu = False
ses = Browser()
ses.setkuki = 'datr=3STGXkMPoaOiUi1LsuyTXUjW;sb=3STGXm9Ssa7bQfBGl7LIgciU;_fbp=fb.1.1590374194832.1953788605;locale=id_ID;c_user=100042800416881;xs=33%3AKdudfysWx4NP3Q%3A2%3A1597984136%3A20352%3A15792%3A%3AAcUwuYmCgHviTbsQn_CmZb-W1OUtBsa1-Qd54LujPQ;fr=10HWB47diXabtdUCr.AWUdn5VZ0K4fTc7UMQESc-85ldY.BexiTd.Fv.F8_.0.0.BfP8T8.AWUaq1A6;wd=424x786' 
# asmin kuki
# ses.setkuki = 'sb=cU7NXleSoBQERfNyGMLEBylr; datr=cU7NXqzRldSG_OTvsBFyOlkk; c_user=100025893515579; xs=4:RnyhPz-7avlLfw:2:1593556171:7058:11217::AcUwDNBT0XaWhuc6gHxrEQEcjBof2TWCCUwg1aETAQ; fr=03nl1VwibMO00Ssb3.AWXz_XLDWGF6dfVgQ4h_qQkgwAQ.BezUzl.M2.AAA.0.0.BfQKQ8.AWWSMhPo; m_pixel_ratio=2.549999952316284; wd=424x786; x-referer=eyJyIjoiL2hvbWUucGhwIiwiaCI6Ii9ob21lLnBocCIsInMiOiJtIn0='
process_count = 0
"""
  ____        ____ ______
 /_  / ___   / __//_  __/
  / /_/ -_) / _/   / /   
 /___/\__/ /_/    /_/
 A Simple tools for facebook
 """
SUB = [
        {
            "react":
            [
                "Group",
                "Timeline",
                "Friend Timeline",
            ]
            },
        {
            "group":[
                "Post",
                "Leave"
                ]
            },
        {
            "comment":[
                "Group",
                "Timeline",
                "Friend Timeline"
                ]
            },
        {
            "messages":[
                "Spam user",
                "Spam group",
                "Online user",
                "Delete chat",
                "Delete empty chat",
                "Broadcast messages"
                ]
            },
        {
            "friend":[
                "Unfriend",
                "Delete requests",
                "Confirm requests",
                "Cancel Requests"
                ]
            },
        {
            "image":[
                "Album",
                "From Inbox",
                "Friend Album",
                ]
            }
        ]
MENU = [
        "React",
        "Group",
        "Comment",
        "Messages",
        "Friendship",
        "Image Downloader",
        "Find ID or Username",
        ]
def banner(logo=False):
        #print(f'''
        

#  {R}||{r}..{R}||{B}  ZeFT{R}|{r}v.0.3\033[35;2mBeta.
#  {R}\\\{r}(){R}//{B}  Github: zettamus
# {R}//{r}(..){R}\\\\{r} Facebook: fb.me/zettid.1
# {R}||    ||{r} Mode : anjay
# \033[32;7m          From XiuzCode          {r}
#''')
    print(f"""
  {Fore.LIGHTBLUE_EX}╔═╗{Fore.RESET}┌─┐┌─┐┌┬┐
  {Fore.LIGHTBLUE_EX}╔═╝{Fore.RESET}├┤ ├┤  │
  {Fore.LIGHTBLUE_EX}╚═╝{Fore.RESET}└─ └   ┴ v.0.3 """)
    if logo:
        print(' > user : ' + C + __isName + r )
        print(' > \033[33;mwarn : \033[0;mdon\'t use for ilegal purpose')
    else:
        print(f" {Back.BLUE+Fore.WHITE}   Coded by "+random.choice(["asmin","zett"]).title()+"   ")
        print()
def back(info, function):
    getpass(f' {r}[{R}!{r}] {info}. Back..!')
    function()
def process(total):
        global process_count
        process_count += 1 
        print(f"\r [!] {str(process_count)}/{str(len(total))} Process ",end="")
        if process_count == total:
            process_count = 0
def select(maxchoice):
    loop = 3
    while loop >= 1:
        loop -= 1
        try:
            cursor = input(f'{B} >>> {r}')
            if cursor == '':
                continue
            elif cursor.isdigit():
                if maxchoice >= int(cursor):
                    return cursor
                else:
                    getpass(f' [{R}!{r}] Wrong choice..!')
            else:
                getpass(f' [{R}!{r}] Please use number..!')
        except (KeyboardInterrupt, EOFError):
            exit(f' {r}[{R}!{r}] {R}Exit by user{r}')
    else:
        back('Max input',Menu)
def Sort(current):
    count = 0
    for menu in current:
        count += 1
        print(f" {C + str(count) + r}). {menu.title()}")
    print(f" {R}0{r}). Back")
    return count
def getinput(string):
    return input(f'{r} [{C}?{r}] {r}{string} :{C} ')
def progress():
    global penentu, STATUS
    count = 0
    cursor.hide()
    while True:
        count += 1
        char = ''
        for _ in range(4):
            if STATUS != None:
                print(end='\r %s[%s%s%s] Please wait%s   '%(r,C,STATUS,r,char));time.sleep(.4)
            else:
                print(end='\r %s[%s!%s] Please wait%s   '%(r,C,r,char));time.sleep(.4)
            char += "."
        count = 0
        if penentu == True:
            STATUS = None
            penentu = False
            cursor.show()
            break
def list_react():
    REACTIONS = ['haha','wow','sad','care','super','like','angry']
    return REACTIONS[int(select(Sort(REACTIONS))) - 1]
def getemptychat(data):
    if not "last_message_timestamp" in str(ses.get(data["url"]).content):
        return data
def broadcast(name):
    jml = 0
    with open('broadcast/' + name, 'a') as f:
        while True:
            jml += 1
            usr = input(f' {r}[{C+str(jml)+r}] Username/ID  : ')
            if usr == '':
                break
            else:
                f.write(usr + '\n')
def Menu():
    Th = Thread(target=progress)
    Th.daemon = True
    os.system('clear')
    global penentu, STATUS
    banner()
    cursor = select(Sort(MENU))
    if cursor == '1':
        react = facebook.React(ses)
        cursor = select(Sort(SUB[0]["react"]))
        if cursor == '1':
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f' {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            react_type = list_react()
            amount = int(getinput('amount (Ex:20)'))
            Th.start()
            data = react.in_group(react_type,choice,amount)
            penentu = True
            print()
            for x in data:
                ses.get(x)
                process(data)
        elif cursor == '2':
            react_type = list_react()
            amount = int(getinput('amount (Ex:20)'))
            Th.start()
            data = react.in_home(react_type, amount)
            penentu = True
            print()
            for x in data:
                ses.get(x)
                process(data)
            Menu()
        elif cursor == '3':
            react_type = list_react()
            val = facebook.user(ses.get(getinput('username')).content)
            amount = int(getinput('amount (Ex:20)'))
            Th.start()
            data = react.in_people(react_type,val["id"], amount)
            penentu = True
            print()
            for x in data:
                ses.get(x)
                process(data)
            Menu()
        elif cursor == '0':
            Menu()
    elif cursor == '2':
        cursor = select(Sort(SUB[1]["group"]))
        if cursor == '1':
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f' {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            text = getinput('text')
            action, form = facebook.group.post_group(ses, choice, text)
            ses.post(action, form)
        elif cursor == '2':
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f' {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            action, form = facebook.group.leave_group(ses, choice)
            ses.post(action, form)
        elif cursor == '0':
            Menu()
    elif cursor == '3':
        comment = facebook.Comment(ses)
        cursor = select(Sort(SUB[2]["comment"]))
        if cursor == '1':
            amount = getinput('amount (Ex:20)')
            value = getinput("comment text")
            Th.start()
            data = comment.in_home(amount,value)
            penentu = True
            print()
            for x in data:
                action = x["action"]
                del x["action"]
                process(data)
                ses.post(action, x)
        elif cursor == '2':
            user = getinput('Username/ID')
            amount = getinput('Amount (Ex:20)')
            value = getinput("Comment text")
            Th.start()
            data = comment.in_people(user,amount)
            penentu = True
            for x in data:
                action = x["action"]
                del x["action"]
                process(data)
                ses.post(action, x)
        elif cursor == '3':
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f' {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            value = getinput('Comment')
            amount = int(getinput('amount (Ex:20)'))
            Th.start()
            data = comment.in_group(choice,amount,value)
            penentu = True
            print()
            for x in data:
                action = x["action"]
                del x["action"]
                process(data)
                ses.post(action, x)
        elif cursor == '0':
            Menu()
    elif cursor == '4':
        messages = facebook.Messages()
        cursor = select(Sort(SUB[3]["messages"]))
        if cursor == '1':
            id = getinput('Username/ID')
            id = facebook.user(ses.get('profile.php?id=' + id if id.isdigit() else id).content)["id"]
            message = getinput('Messages')
            amount = getinput('Amount')
            Th.start()
            STATUS = 'Sending'
            messages.people(ses,id, message,int(amount))
            STATUS = "Complete"
            penentu = True
        elif cursor == '2':
            id = getinput('ID Group')
            message = getinput('Messages')
            amount = getinput('Amount')
            messages.group(ses,id,message, int(amount))
        elif cursor == '3':
            data = messages.getusersonline(ses)
            if len(data) == 0:
                print('no friend online')
            else:
                msg = getinput('Messages')
                for user in data:
                    messages.people(ses, user, msg)
        elif cursor == '4':
            Th.start()
            STATUS = 'Get Messages'
            data = messages.getmsg(ses)
            penentu = True
            with ThreadPoolExecutor(10) as ex:
                for url in data:
                    ex.submit(messages.delete_msg,(ses, url["url"]))
        elif cursor == '5':
            Th.start()
            STATUS = 'Get Messages'
            data = messages.getmsg(ses)
            STATUS = 'Get Empty Chat'
            rv = []
            with ThreadPoolExecutor(max_workers=10) as executor:
                for url in data:
                    res = executor.submit(getemptychat,(url))
                    if res.result() != None:
                        rv.append(res.result())
            if len(rv) == 0:
                exit('you not have empty chat')
            penentu = True
            print("")
            ask = getinput('Showlogs (Y/n)').lower()
            for x in rv:
                if ask == 'y':
                    print(f' {r}[{C}!{r}] {x["text"]} ')
                else:
                    process(rv)
                messages.delete_msg(ses, x["url"])
        elif cursor == '6':
            list_ = os.listdir('./broadcast')
            count = len(list_)
            if len(list_) == 0:
                print(f' {r}[{R}!{r}] You not have list broadcast')
                ask = getinput('Do you want to make list broadcast (Y/n)').lower()
                if ask == 'y':
                    name = getinput('Broadcast name')
                    if name == '':
                        count += 1
                        name = f'broadcast-{count}'
                    broadcast(name)
                    back('Done',Menu)
                else:
                    back('Oke',Menu)
            else:
                print(f' {r}[{Fore.LIGHTGREEN_EX}!{r}] type "new" to make new broadcast')
                Sort(list_)
                cursor = input(f'{B} >>> {r}')
                if cursor == 'new':
                    name = getinput('Broadcast name')
                    if name == '':
                        count += 1
                        name = f'broadcast-{count}'
                        broadcast(name)
                else:
                    try:
                        files = open("broadcast/" + list_[ int(cursor) - 1 ]).read().splitlines()
                    except:
                        back(f'"{cursor}" out of index',Menu)
                    message = getinput('Messages')
                    count = 0
                    for user in files:
                        count += 1
                        print(" %s[%s%s%s] %s"%(r,C,count,r,user))
                        messages.people(ses, facebook.user(ses.get(user).content)["id"], message)
                    back('Done',Menu)
    elif cursor == '5':
        cursor = select(Sort(SUB[4]["friend"]))
        if cursor == '1':
            data = facebook.friends.unfriend(ses)
            print(data)
        elif cursor == '2':
            Th.start()
            data = facebook.friends.delete(ses)
            penentu = True
            print("")
            print("")
            back(str(len(data)), Menu)
        elif cursor == '3':
            Th.start()
            data = facebook.friends.confirm(ses)
            penentu = True
            print("")

            back(str(len(data)), Menu)
        elif cursor == '4':
            Th.start()
            data = facebook.friends.cancel(ses)
            penentu = True
            print("")
            back(str(len(data)), Menu)
    elif cursor == '6':
        cursor = select(Sort(SUB[5]["image"]))
        if cursor == '1':
            data = facebook.Showalbum(ses, 'me')
            count = 0
            for nama in data:
                count += 1
                print(f' {C+str(count)+r}). {nama["text"]}')
            cursor = data[int(select(len(data))) - 1]["url"]
            data = facebook.images.album(ses, cursor)
            count = 0
            if len(data) != 0:
                for x in data:
                    process(data)
                    count += 1
                    with open('Photos/' + time.strftime('%Y%M%S') + str(count) + ".jpg", "wb") as f:
                        f.write(facebook.action.download(x))
        elif cursor == '2':
            user = getinput('Username/ID')
            name = facebook.user(ses.get(user).content)["name"]
            data = facebook.images.inbox(ses, user)
            count = 0
            if len(data) != 0:
                for x in data:
                    process(data)
                    count += 1
                    with open('Photos/' + name + "-" + time.strftime('%Y%M%S') + str(count) + ".jpg", "wb") as f:
                        f.write(facebook.action.download(x))
        elif cursor == '3':
            user = getinput('Username/ID')
            nama = facebook.user(ses.get(user))["name"]
            data = facebook.Showalbum(ses, 'me')
            count = 0
            for nama in data:
                count += 1
                print(f' {C+str(count)+r}). {nama["text"]}')
            cursor = data[int(select(len(data))) - 1]["url"]
            data = facebook.images.album(ses, cursor)
            count = 0
            if len(data) != 0:
                for x in data:
                    process(data)
                    count += 1
                    with open('Photos/' + nama + '-' + time.strftime('%Y%M%S') + str(count) + ".jpg", "wb") as f:
                        f.write(facebook.action.download(x))
    if cursor == '7':
        print(facebook.Finduser(ses, "asmin"))
try:
    Menu()
except IOError: cursor.show()
