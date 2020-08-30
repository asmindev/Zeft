import json


def addsess(name, username, id, cookie):
    try:
        add = eval(open("lib/users.log").read())
    except (FileNotFoundError, SyntaxError):
        with open("lib/users.log", "a") as add:
            add.write('[{"name":"' + name + '","username":"' + username + '","id":"' + id + '","cookie":"' + cookie + '"}]')
    else:
        if cookie in str(add):
            raise ValueError("Cookie already exists")
        else:
            new = '{"name":"' + name + '","username":"' + username + '","id":"' + id + '","cookie":"' + cookie + '"}'
            add.append(json.loads(new))
            with open("lib/users.log", "w") as new:
                new.write(str(add))
                return True


def remove(cookie):
    arg = []
    kuki = eval(open("lib/users.log").read())
    for cook in kuki:
        if cook["cookie"] == cookie:
            continue
        else:
            arg.append(cook)
    with open("lib/users.log", "w") as f:
        f.write(str(arg) if len(arg) != 0 else "")
