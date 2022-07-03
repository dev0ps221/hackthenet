#!/usr/bin/env python3

from .Command import *
class Shell:
    cmds = {}
    def setPrompt(self,prompt = '>'):
        self.prompt = prompt
    
    def shellLoop(self):
        while self.run == True:
            cmd = self.getCmd()
            # print(self.cmds.__contains__(cmd))
            command = self.cmds.get(cmd)
            if command != None:
                print(type(command) == type(lambda x:x))
                if type(command) == type(lambda x:x):
                    command.run(self)
                    print(command)
                    print('is command')
            else:  
                print('Commande Inconnue')
                

    def avail_commands(self):
        comms = ""
        for key in self.cmds.keys():
            comms += "\n\t{}".format(key)
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
            self.cmds[cmd] = cmds[cmd]
            self.cmds[cmd].shell = self

    def getCmd(self):
        return input("{}".format(self.prompt))

    def __init__(self,cmds={},mod='no module'):
        self.run = False
        self.registerCommands(cmds)
        self.mod = mod
        self.setPrompt()





if __name__ == '__main__':
    cmds = {
        'exit':Command('exit',lambda self : self.shell.stop()),
        'quit':Command('quit',lambda self : self.shell.stop()),
        'pymod':Command('pymod',lambda self,name=5 : print(self.shell))
    }
    shell = Shell(cmds)
    shell.loop()