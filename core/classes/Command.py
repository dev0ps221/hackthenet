#!/usr/bin/env
class Command:


    def run(self,args=None):
        self.action(self)

    def __init__(self,name,func):
        self.name = name 
        self.action = func


