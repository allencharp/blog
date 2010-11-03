# -*- coding:utf-8 -*-

from datetime import datetime
from library import *
from logic import *
from mvc import *

@url(["/", r"(?i)/index.htm[l]?"])
class IndexHandler(BaseHandler):
    def get(self):
        self.view("index.html", time = datetime.now().isoformat(" "))

@url(r"(?i)/test/json/(?P<i>\d+)")
class TestHandler(BaseHandler):
    @nocache
    def get(self, i):
        self.json(message="server", i=int(i)+1)
