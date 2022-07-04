#!/usr/bin/env
class Command:


    def run(self,*args):
        self.action(self,*args)

    def __init__(self,name,func):
        self.name = name 
        self.action = func


