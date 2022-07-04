#!/usr/bin/env python3
from pcapy import findalldevs
from os import system
from .Command import *

def clear():
    system('clear')


shellCmds = [
    ['exit',Command('exit',lambda self : self.shell.stop(),'exits the terminal')],
    ['quit',Command('quit',lambda self : self.shell.stop()),'alias for (exit)'],
    ['clear',Command('clear',lambda self : clear()),'clears the terminal screen'],
    ['pymod',Command('pymod',lambda self,name=None : print(self.shell if not name else "module {}".format(name)))],
    ['ifaces',Command('ifaces',lambda self : [print("-{}".format(dev)) for dev in findalldevs()])]
]

class Shell:
    cmds = {}
    def setPrompt(self,prompt = '>'):
        self.prompt = prompt
    
    def shellLoop(self):
        while self.run == True:
            cmd,args = self.getCmd()
            command = self.cmds.get(cmd)
            if command != None:
                if type(command) == Command:
                    result = command.run(*args)
            else:  
                result =  'Commande Inconnue'
            self.process_results(result)
                
    def process_results(self,result):
        print(result)

    def avail_commands(self):
        comms = ""
        for key in self.cmds.keys():
            comms += "\n\t{}".format(self.cmds[key].descript())
        return comms

    def __str__(self):
        return (f"Shell object for {self.mod} \n Available Commands:{ self.avail_commands() }")

    def stop(self):
        self.run = False

    def loop(self):
        self.run = True
        self.shellLoop()

    def registerCommands(self,cmds):
        for cmd in cmds:
            self.addCommand(cmd,cmds[cmd])
    
    def addCommand(self,cmd,func):
        self.cmds[cmd] = func
        self.cmds[cmd].shell = self

    def parseInput(self,data):
        datalist = data.split(' ')
        cmd = datalist[0]
        args = datalist[1:]
        return cmd,args

    def initCmds(self):
        for name,action in shellCmds:
            self.addCommand(name,action)

    def getCmd(self):
        return self.parseInput(input("{}".format(self.prompt)))

    def __init__(self,cmds={},mod='nomod'):
        self.run = False
        self.initCmds()
        self.registerCommands(cmds)
        self.mod = mod
        self.setPrompt()





if __name__ == '__main__':
    shell = Shell()
    shell.loop()