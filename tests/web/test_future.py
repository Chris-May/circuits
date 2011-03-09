#!/usr/bin/env python

from urllib.request import urlopen

from circuits.web import Controller
from circuits import future, Event, Component

class Hello(Event):
    """Hello Event"""

class Test(Component):

    def hello(self):
        return "Hello World!"

class Root(Controller):

    @future()
    def index(self):
        return self.push(Hello())

def test(webapp):
    Test().register(webapp)

    f = urlopen(webapp.server.base)
    s = f.read()
    assert s == b"Hello World!"
