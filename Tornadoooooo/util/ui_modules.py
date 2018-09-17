# !*/user/bin/python3
# -*- coding: utf-8 -*-
from tornado.web import  UIModule

class UIModule(UIModule):
    def render(self,*args,**kwargs):
        return "woshiuim"