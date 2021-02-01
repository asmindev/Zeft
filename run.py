#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Coded by ['Asmin','Zett']
# Github : zettamus
# Facebook : fb .me/zettid.1
# Telegram : t.me/zettamus
# if you want to recode please dont change name author
# +---------------------------------+

import os
import time
import random
import facebook
from lib import addses
from getpass import getpass
from threading import Thread
from facebook.request import Browser
from colorama import Back, Fore, init
from concurrent.futures import ThreadPoolExecutor


akun = facebook.Account()
init(True)

# var global
STATUS = None
penentu = False
DATA_USER = None
process_count = 0
ses = Browser()


SUB = [
    {"react": ["Group", "Timeline", "Friend Timeline"]},
    {"group": ["Post", "Leave"]},
    {"comment": ["Group", "Timeline", "Friend Timeline"]},
    {
        "messages": [
            "Spam user",
            "Spam group",
            "Online user",
            "Delete chat",
            "Delete empty chat",
            "Broadcast messages",
        ]
    },
    {"friend": ["Unfriend", "Delete requests",
                "Confirm requests", "Cancel Requests"]},
    {"image": ["Album", "From Inbox", "Friend Album"]},
]

MENU = [
    "React",
    "Group",
    "Comment",
    "Messages",
    "Friendship",
    "Image Downloader",
    "Find user",
]

TITLE = ["Main menu", "Login"]


def banner(logo=False):
    print(
        f"""
  {Fore.LIGHTBLUE_EX}╔═╗{Fore.RESET}┌─┐┌─┐┌┬┐
  {Fore.LIGHTBLUE_EX}╔═╝{Fore.RESET}├┤ ├┤  │
  {Fore.LIGHTBLUE_EX}╚═╝{Fore.RESET}└─ └   ┴ v.0.3 """
    )
    if logo:
        print(
            f" {Back.WHITE+Fore.BLACK}   Coded by "
            + random.choice(["asmin", "zett"]).title()
            + "   "
        )
        print()
        show(
            "Name : " + DATA_USER["name"] + " (" + DATA_USER["username"] + ")"
            if DATA_USER["username"] is not None
            else "Name : " + DATA_USER["name"]
        )
        show("UID  : " + DATA_USER["id"])
        print()
    else:
        print(
            f" {Back.WHITE+Fore.BLACK}   Coded by "
            + random.choice(["asmin", "zett"]).title()
            + "   "
        )
        print()


def show(info):
    print(f" {r}[{C}*{r}] {info}")


def back(info, function=None):
    getpass(f" {r}[{R}!{r}] {info}. Back..!")
    function() if function is not None else ""


def process(total):
    global process_count
    process_count += 1
    print(
        f"{Fore.RESET}[{Fore.LIGHTGREEN_EX}!{Fore.RESET}] {str(process_count)}/{str(len(total))} Process ",
        end="\r ",
    )
    if process_count == total:
        process_count = 0


def select(maxchoice, menu=True):
    loop = 3
    while loop >= 1:
        loop -= 1
        try:
            cursor = input(f"{B} >>> {r}")
            if cursor == "":
                continue
            elif cursor.isdigit():
                if maxchoice >= int(cursor):
                    return cursor
                else:
                    getpass(f" [{R}!{r}] Wrong choice..!")
            else:
                getpass(f" [{R}!{r}] Please use number..!")
        except (KeyboardInterrupt, EOFError):
            exit(f" {r}[{R}!{r}] {R}Exit by user{r}")
    else:
        back("Max input", Menu if menu else Ahead)


def Sort(current, back=True):
    count = 0
    for menu in current:
        count += 1
        print(f" {C + str(count) + r}). {menu.title()}")
    if back:
        print(f" {R}0{r}). Back")
    else:
        print(f" {R}0{r}). Exit")
    return count


def getinput(string):
    while True:
        text = input(f"{r} [{C}?{r}] {r}{string} :{C} ")
        if text != "":
            return text


def progress():
    global penentu, STATUS
    count = 0
    while True:
        count += 1
        char = ""
        for _ in range(4):
            if STATUS is not None:
                print(
                    "%s[%s%s%s] Please wait%s   " % (r, C, STATUS, r, char), end="\r "
                )
                time.sleep(0.4)
            else:
                print("%s[%s!%s] Please wait%s   " %
                      (r, C, r, char), end="\r ")
                time.sleep(0.4)
            char += "."
        count = 0
        if penentu:
            STATUS = None
            penentu = False
            return


def list_react():
    print()
    REACTIONS = ["haha", "wow", "sad", "care", "super", "like", "angry"]
    return REACTIONS[int(select(Sort(REACTIONS))) - 1]


def getemptychat(data):
    if "last_message_timestamp" not in str(ses.get(data["url"]).content):
        return data


def broadcast(name):
    jml = 0
    with open("broadcast/" + name, "a") as f:
        while True:
            jml += 1
            usr = input(f" {r}[{C+str(jml)+r}] Username/ID  : ")
            if usr == "":
                break
            else:
                f.write(usr + "\n")


def Menu():
    global penentu, process_count, STATUS
    process_count = 0
    Th = Thread(target=progress)
    Th.daemon = True
    os.system("clear")
    banner(True)
    cursor = select(Sort(MENU))
    if cursor == "1":
        react = facebook.React(ses)
        cursor = select(Sort(SUB[0]["react"]))
        if cursor == "1":
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f'   {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            react_type = list_react()
            amount = int(getinput("amount (Ex:20)"))
            Th.start()
            data = react.in_group(react_type, choice, amount)
            penentu = True
            print("\n")
            for x in data:
                process(data)
                ses.get(x)
            back("Done", Menu)
        elif cursor == "2":
            react_type = list_react()
            amount = int(getinput("amount (Ex:20)"))
            Th.start()
            data = react.in_home(react_type, amount)
            penentu = True
            print("\n")
            for x in data:
                process(data)
                ses.get(x)
            print("\n")
            back("Done", Menu)
        elif cursor == "3":
            val = facebook.user(ses.get(getinput("username")).content)
            show("Target: " + val["name"])
            react_type = list_react()
            amount = int(getinput("amount (Ex:20)"))
            Th.start()
            data = react.in_people(react_type, val["id"], amount)
            penentu = True
            print("\n")
            for x in data:
                process(data)
                ses.get(x)
            print("\n")
            back("Done", Menu)
        elif cursor == "0":
            Menu()
    elif cursor == "2":
        cursor = select(Sort(SUB[1]["group"]))
        if cursor == "1":
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f'   {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            text = getinput("text")
            action, form = facebook.group.post_group(ses, choice, text)
            ses.post(action, form)
            back("Done", Menu)
        elif cursor == "2":
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f'   {C+str(count)+r}). {grub["name"]}')
            show("use comma (,) as separator")
            choice = set([int(choice)
                          for choice in input(f"{B} >>> {r}").split(",")])
            for out in choice:
                try:
                    print('     :Leave from: %s...' % current[out - 1]["name"], end='')
                    choice = current[out - 1]["url"]
                    action, form = facebook.group.leave_group(ses, choice)
                    ses.post(action, form)
                    print(' done')
                except IndexError:
                    show('"%s" out of list ' % out)
                    continue
            back("Done", Menu)
        elif cursor == "0":
            Menu()
    elif cursor == "3":
        comment = facebook.Comment(ses)
        cursor = select(Sort(SUB[2]["comment"]))
        if cursor == "1":
            user = getinput("Username/ID")
            amount = getinput("Amount (Ex:20)")
            value = getinput("Comment text")
            Th.start()
            data = comment.in_people(user, amount, value)
            penentu = True
            print("\n")
            for x in data:
                action = x["action"]
                del x["action"]
                process(data)
                ses.post(action, x)
            print("\n")
            back("Done", Menu)
        elif cursor == "2":
            value = getinput("Comment text")
            amount = getinput("Amount (Ex:20)")
            Th.start()
            data = comment.in_home(amount, value)
            penentu = True
            print("\n")
            for x in data:
                action = x["action"]
                del x["action"]
                process(data)
                ses.post(action, x)
            print("\n")
            back("Done", Menu)
        elif cursor == "3":
            count = 0
            current = facebook.Showgroup(ses)
            for grub in current:
                count += 1
                print(f'   {C+str(count)+r}). {grub["name"]}')
            choice = current[int(select(len(current))) - 1]["url"]
            value = getinput("Comment")
            amount = int(getinput("Amount (Ex:20)"))
            Th.start()
            data = comment.in_group(choice, amount, value)
            penentu = True
            print("\n")
            for x in data:
                action = x["action"]
                del x["action"]
                ses.post(action, x)
                process(data)
            print("\n")
            back("Done", Menu)
        elif cursor == "0":
            Menu()
    elif cursor == "4":
        messages = facebook.Messages()
        cursor = select(Sort(SUB[3]["messages"]))
        if cursor == "1":
            id = getinput("Username/ID")
            id = facebook.user(
                ses.get("profile.php?id=" + id if id.isdigit() else id).content
            )
            show("Target: " + id["name"])
            message = getinput("Messages")
            amount = getinput("Amount")
            Th.start()
            STATUS = "Sending"
            messages.people(ses, id["id"], message, int(amount))
            STATUS = "Complete"
            penentu = True
            back("Done", Menu)
        elif cursor == "2":
            id = getinput("ID Group")
            message = getinput("Messages")
            amount = getinput("Amount")
            messages.group(ses, id, message, int(amount))
            back("Done", Menu)
        elif cursor == "3":
            data = messages.getusersonline(ses)
            if len(data) == 0:
                back("No friend online", Menu)
            else:
                msg = getinput("Messages")
                for user in data:
                    messages.people(ses, user, msg)
            back("Done", Menu)
        elif cursor == "4":
            Th.start()
            STATUS = "Get Messages"
            data = messages.getmsg(ses)
            penentu = True
            print("\n")
            with ThreadPoolExecutor(10) as ex:
                for url in data:
                    ex.submit(messages.delete_msg, (ses, url["url"]))
            back("Done", Menu)
        elif cursor == "5":
            Th.start()
            STATUS = "Get Messages"
            data = messages.getmsg(ses)
            STATUS = "Get Empty Chat"
            rv = []
            with ThreadPoolExecutor(max_workers=10) as executor:
                for url in data:
                    res = executor.submit(getemptychat, (url))
                    if res.result() is not None:
                        rv.append(res.result())
            if len(rv) == 0:
                back("You not have empty chat", Menu)
            penentu = True
            print("")
            ask = getinput("Showlogs (Y/n)").lower()
            for x in rv:
                if ask == "y":
                    print(f'  {x["text"]} ')
                else:
                    process(rv)
                messages.delete_msg(ses, x["url"])
            back("Done", Menu)
        elif cursor == "6":
            try:
                os.mkdir("broadcast")
            except:
                pass
            list_ = os.listdir("./broadcast")
            count = len(list_)
            if len(list_) == 0:
                print(f" {r}[{R}!{r}] You not have list broadcast")
                ask = getinput(
                    "Do you want to make list broadcast (Y/n)").lower()
                if ask == "y":
                    name = getinput("Broadcast name")
                    if name == "":
                        count += 1
                        name = f"broadcast-{count}"
                    broadcast(name)
                    back("Done", Menu)
                else:
                    back("Oke", Menu)
            else:
                print(
                    f' {r}[{Fore.LIGHTGREEN_EX}!{r}] type "new" to make new broadcast'
                )
                Sort(list_)
                cursor = input(f"{B} >>> {r}")
                if cursor == "new":
                    name = getinput("Broadcast name")
                    if name == "":
                        count += 1
                        name = f"broadcast-{count}"
                    broadcast(name)
                    back("Done", Menu)
                else:
                    try:
                        files = (
                            open("broadcast/" + list_[int(cursor) - 1])
                            .read()
                            .splitlines()
                        )
                    except Exception:
                        back(f'"{cursor}" out of index', Menu)
                    message = getinput("Messages")
                    count = 0
                    print()
                    for user in files:
                        count += 1
                        print("   %s%s%s). %s" % (C, count, r, user))
                        messages.people(
                            ses, facebook.user(ses.get(user).content)[
                                "id"], message
                        )
                    back("Done", Menu)
    elif cursor == "5":
        cursor = select(Sort(SUB[4]["friend"]))
        if cursor == "1":
            data = facebook.friends.unfriend(ses)
            print(data)
        elif cursor == "2":
            Th.start()
            data = facebook.friends.delete(ses)
            penentu = True
            back(str(len(data)), Menu)
        elif cursor == "3":
            Th.start()
            data = facebook.friends.confirm(ses)
            penentu = True
            print("")
            back(str(len(data)), Menu)
        elif cursor == "4":
            Th.start()
            data = facebook.friends.cancel(ses)
            penentu = True
            print("")
            back(str(len(data)), Menu)
        elif cursor == "0":
            Menu()
    elif cursor == "6":
        cursor = select(Sort(SUB[5]["image"]))
        if cursor == "1":
            data = facebook.Showalbum(ses, "me")
            count = 0
            for nama in data:
                count += 1
                print(f'   {C+str(count)+r}). {nama["text"]}')
            cursor = data[int(select(len(data))) - 1]["url"]
            data = facebook.images.album(ses, cursor)
            count = 0
            if len(data) != 0:
                for x in data:
                    process(data)
                    count += 1
                    with open(
                        "Photos/" +
                            time.strftime("%Y%M%S") + str(count) + ".jpg", "wb"
                    ) as f:
                        f.write(facebook.action.download(x))
            back("Done", Menu)
        elif cursor == "2":
            user = getinput("Username/ID")
            name = facebook.user(ses.get(user).content)["name"]
            data = facebook.images.inbox(ses, user)
            count = 0
            if len(data) != 0:
                for x in data:
                    process(data)
                    count += 1
                    with open(
                        "Photos/"
                        + name
                        + "-"
                        + time.strftime("%Y%M%S")
                        + str(count)
                        + ".jpg",
                        "wb",
                    ) as f:
                        f.write(facebook.action.download(x))
            print("\n")
            back("Done", Menu)
        elif cursor == "3":
            user = getinput("Username/ID")
            name = facebook.user(ses.get(user).content)["name"].split(" ")[0]
            data = facebook.Showalbum(ses, user)
            count = 0
            for nama in data:
                count += 1
                print(f'   {C+str(count)+r}). {nama["text"]}')
            cursor = data[int(select(len(data))) - 1]["url"]
            data = facebook.images.album(ses, cursor)
            count = 0
            if len(data) != 0:
                for x in data:
                    process(data)
                    count += 1
                    with open(
                        "Photos/"
                        + str(name)
                        + "-"
                        + time.strftime("%Y%M%S")
                        + str(count)
                        + ".jpg",
                        "wb",
                    ) as f:
                        f.write(facebook.action.download(x))
            print("\n")
            back("Done", Menu)
        elif cursor == "0":
            Menu()
    elif cursor == "7":
        nama = facebook.Finduser(ses, getinput("Enter full name"))
        print()
        for user in nama:
            print(f" {r}[{C}*{r}] {user['name']} ")
            if "id" in user:
                print(f" {r}[{C}*{r}] {user['id']} ")
            else:
                print(f" {r}[{C}*{r}] {user['username']} ")
            print("-" * 30)
        back("Done", Menu)
    elif cursor == "0":
        Ahead()


def Ahead():
    global DATA_USER
    os.system("clear")
    banner()
    choice = select(Sort(TITLE, back=False), menu=False)
    if choice == "1":
        print(
            f'  You have session "{DATA_USER["name"]}"\n' if akun.logged else "")
        try:
            listuser = open("lib/users.log").read()
            if listuser == "":
                os.remove("lib/users.log")
                exit(" Run again")
            listuser = eval(listuser)
            if len(listuser) != 1:
                count = 0
                for user in listuser:
                    count += 1
                    print(f'  {C + str(count) + r}) {user["name"]}')
                kuki = listuser[int(
                    select(len(listuser), menu=False)) - 1]["cookie"]
            else:
                kuki = listuser[0]["cookie"]
            ses.setkuki = kuki
            DATA_USER = akun.login(ses)
            if DATA_USER:
                Menu()
            else:
                addses.remove(ses.showkuki["cookie"])
                back("Cookie invalid!", Ahead)
        except FileNotFoundError:
            back("File cookies not found", Ahead)
    elif choice == "2":
        for i in range(3):
            cookies = getinput("Put your cookie")
            if "datr" in cookies and "c_user" in cookies:
                ses.setkuki = cookies
                DATA_USER = akun.login(ses)
                if DATA_USER:
                    addses.addsess(
                        DATA_USER["name"],
                        str(DATA_USER["username"]),
                        DATA_USER["id"],
                        ses.showkuki["cookie"],
                    )
                    return Menu()
            show("Cookie wrong")
        back("Please check your cookie before try again",
             Ahead) if i == 0 else Ahead()


if "__main__" == __name__:
    R = "\033[31;m"
    C = "\033[36;m"
    G = "\033[35;m"
    B = "\033[94;m"
    r = "\033[0;m"
    try:
        os.mkdir("Photos")
    except Exception:
        pass
    Ahead()
else:
    exit("Please running as file, not import")
