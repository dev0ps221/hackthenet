#!/usr/bin/env python3
from pcapy import findalldevs
from os import system
from Command import *

def clear():
    system('clear')


def pymod(self,name=None) :
    return self.shell if not name else "module {}".format(name)

def ifaces(self):
    return '\n'.join(["-{}".format(dev) for dev in findalldevs()])

def _exit(self):
    self.shell.stop()

shellCmds = [
    ['exit',Command('exit',_exit,'exits the terminal')],
    ['quit',Command('quit',_exit,'alias for (exit)')],
    ['clear',Command('clear',clear,'clears the terminal screen')],
    ['pymod',Command('pymod',pymod)],
    ['ifaces',Command('ifaces',ifaces)]
]

class Shell:
    cmds = {}
    def setPrompt(self,prompt = '>'):
        self.prompt = prompt
    
    def shellLoop(self):
        while self.run == True:
            cmd,args = self.getCmd()
            self.process_cmd(cmd,args)
    
    def process_cmd(self,cmd,*args):
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
        for cmd in shellCmds:
            name,action = cmd 
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