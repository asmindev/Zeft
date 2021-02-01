from .parser_html import Parsing

def post_group(ses, idgrub, caption):
    raw = Parsing(ses.get(idgrub).content).parsing_form("composer/mbasic")
    raw["xc_message"] = caption
    action = raw["action"]
    del raw["action"]
    del raw["view_photo"]
    del raw["view_overview"]
    return action, raw


def leave_group(ses, idgrub):
    idg = idgrub.split("groups/")[1]
    if idg.isdigit():
        pass
    else:
        idg = Parsing(ses.get(idgrub).content).find_url('members/search/?')[0].split('id=')[1].split('&')[0]
    raw = Parsing(
        ses.get("group/leave/?group_id=" + idg).content
    ).parsing_form("leave")
    act = raw["action"]
    del raw["action"]
    return act, raw
