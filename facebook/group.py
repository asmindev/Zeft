from .parsing import form
def post_group(ses, idgrub, caption):
    raw = form(ses.get(idgrub).content, 'composer/mbasic')
    raw["xc_message"] = caption
    action = raw["action"]
    del raw["action"], raw["view_photo"], raw["view_overview"]
    return action, raw
def leave_group(ses, idgrub):
    raw = form(ses.get('group/leave/?group_id=' + idgrub.split('groups/')[1]).content,'leave')
    act = raw["action"]
    del raw["action"]
    return act, raw
