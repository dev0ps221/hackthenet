#!/usr/bin/env
class Command:


    def run(self,args):
        console.log(self.action,' is command')
        self.action(args)

    def __init__(self,name,func):
        print('command created')
        self.name = name 
        self.action = func


