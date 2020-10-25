#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: zettamus | asmin

from .get import post, user as checked
from .parsing import form, Urlfind, Parser
class Core:
    def __init__(self, ses, type):
        self._ses = ses
        self._type = type
    def people(self,user, amount):
        return post(self._ses, user + "?v=timeline", self._type, '?cursor=',[],amount)
    def group(self,idgroup, amount):
        return post(self._ses, idgroup, self._type, '?bacr',[],amount)
    def home(self,amount):
        return post(self._ses, 'home.php', self._type, '?aftercursor', [], amount) 

class Comment(Core):
    def __init__(self, ses):
        super().__init__(ses, '#footer_action_list')
    def in_home(self, amount, comment_text):
        return self.main(self.home(amount), comment_text)
    def in_people(self, user, amount, comment_text):
        return self.main(self.people(user,amount), comment_text)
    def in_group(self, idgroup, amount, comment_text):
        return self.main(self.group(idgroup, amount), comment_text)
    def main(self, data, comment_text):
        rv = []
        for link in data:
            data = form(self._ses.get(link).content, 'comment.php')
            try:
                del data["view_photo"]
            except KeyError: pass
            try:
                del data["view_mention"]
            except KeyError: pass
            if len(data) != 0:
                data["comment_text"] = comment_text
                rv.append(data)
        return rv
class React(Core):
    """
    :List Reactions
     Like
     Haha
     Wow
     Super
     Care
     Sad
     Angry
    """
    def __init__(self, ses):
        self.react = {'like':'1','super':'3','care':'16','haha':'4','wow':'3','sad':'7','angry':'8'}
        super().__init__(ses, 'reactions/picker')
    def in_home(self, type,amount):
        return self.main(self.home(amount), type)
    def in_people(self, type, user, amount):
        return self.main(self.people(user,amount), type)
    def in_group(self, type, idgroup, amount):
        return self.main(self.group(idgroup, amount), type)
    def main(self, data, type):
        rv = []
        if len(data) == 0:
            raise ValueError("Cant dump data")
        if type not in self.react.keys():
            raise ValueError('Invalid option')
        for url in data:
            react = Urlfind(Parser(self._ses.get(url).content),'reaction_type=' + self.react[type])
            if len(react) != 0:
                rv.append(react)
        return rv
class Other(Core):
    def __init__(self, ses):
        self.ses = ses
    def private(self, amount, type):
        rv = []
        for current in self.home(amount):
            kur = form(self._ses.get(current).content,'handle_action')
            kur["action_key"] = type
            del kur["cancel"]
            rv.append(kur)
        return rv
    def delete(self, amount):
        return self.private(amount, 'DELETE')
    def untag(self, amount):
        return self.private(amount, "UNTAG")

