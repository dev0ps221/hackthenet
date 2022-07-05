#!/usr/bin/env python3
from pcapy import findalldevs
from os import system,getcwd,listdir
from sys import path,exit
insert = path.insert
here = '/'.join(__file__.split('/')[:-1])
where_mods_are = f'{here}/../mods'
modules = list(filter(lambda el:el is not None,[el[:-3] if el[-3:] == '.py' and el != '__init__.py' else None for el in listdir(where_mods_are)]))

if __name__ == 'Shell':
    from Command import *
else :
    from .Command import *

def clear(self):
    system('clear')
    return True


def pymod(self,name=None) :
    return self.shell if not name else "module {}".format(name)

def _list(self,_type=None):
    if _type:
        types_pre = '*-'
        types_sep = '\n'+types_pre
        
        if self.shell.mod != 'nomod' and _type in self.shell.mod.config:
            types = types_sep.join(self.shell.mod.config[_type])
            ret = f"{types_pre}{types}" if len(types) else f"no {_type} found" 
        elif _type in self.shell.config:
            data = self.shell.config[_type]
            if (type(data) is type([])):
                types = types_sep.join(data)
                ret = f"{types_pre}{types}" if len(types) else f"no {_type} found" 

            elif(type(data) is type({})):
                types = types_sep.join(data)
                ret = f"{types_pre}{types}" if len(types) else f"no {_type} found" 

            else:
                ret = "what were you thinking about ?"

        elif hasattr(self.shell,_type):
            data = getattr(self.shell,_type)
            if type(data) in [list,dict]:
                types = types_sep.join(data)
                ret = f"{types_pre}{types}" if len(types) else f"no {_type} found" 
            else:
                ret = "what were you thinking about ?"

        elif _type in globals():
            data = globals()[_type]
            if type(data) in [list,dict]:
                types = types_sep.join(data)
                ret = f"{types_pre}{types}" if len(types) else f"no {_type} found" 
            else:
                ret = "what were you thinking about ?"

        else :
            ret = "no match found"

        return ret


    else:
        return self.show_usage()


def load(self,name=None) :
    if name :
        if name in modules:
            if self.shell.mod != 'nomod' and self.shell.mod.name == name:
                return "module already loaded"
            insert(0, here+'/../mods')
            mod = (getattr(__import__(name, where_mods_are),(name[0].upper()+name[1:])))
            if(mod):
                _module = mod() 
                return _module.shell.loop()
    else:
        return self.show_usage()


def ifaces(self):
    return '\n'.join(["-{}".format(dev) for dev in findalldevs()])

def _help(command,arg=None):
    if arg:
        cmd = command.shell.cmds.get(arg)
        if cmd != None:
            if type(cmd) == Command:
                return cmd.help()
            else:
                return (command.help())
        else:
            if arg in modules:
                if command.shell.mod != 'nomod' and command.shell.mod.arg == arg:
                    return "module already loaded"
                insert(0, here+'/../mods')
                mod = (getattr(__import__(arg, where_mods_are),(arg[0].upper()+arg[1:])))
                if(mod):
                    _module = mod() 
                    return _module.help()
                else:
                    return (command.help())
            else:
                return (command.help())
    else:
        return (command.help())
        

def _exit(command):
    command.shell.stop()
    if(command.shell.mod=='nomod'):
        exit(1)
    else:
        command.shell.mod='nomod'

shellCmds = [
    ['exit',Command('exit',_exit,'exits the terminal')],
    ['quit',Command('quit',_exit,'alias for (exit)')],
    ['clear',Command('clear',clear,'clears the terminal screen')],
    ['help',Command('help',_help,'shows help','\n\t[\t help \t]\nOR\n\t[\t help command \t]')],
    ['pymod',Command('pymod',pymod)],
    ['load',Command('load',load,'loads a module and switch to its shell','\n\t[\t load modulename \t]')],
    ['list',Command('list',_list,'list all the known matches to the requested type','\n\t[\t list typename \t]\n')],
    ['ifaces',Command('ifaces',ifaces)]
]

class Shell:
    cmds = {}
    def setPrompt(self,prompt = 'hackthenet>'):
        self.prompt = prompt
    
    def shellLoop(self):
        while self.run == True:
            cmd,args = self.getCmd()
            self.process_cmd(cmd,*args)
    
    def process_cmd(self,cmd,*args):
        command = self.cmds.get(cmd)
        if command != None:
            if type(command) == Command:
                result = command.run(*args)
        else:  
            if cmd in modules:
                result = self.process_cmd('load',cmd)
            else:
                result =  'Commande Inconnue'
        return self.process_results(command,result)

    def process_results(self,cmd,result):
        print(result) if cmd and cmd.name not in 'quit|exit' and type(result) != bool  else print(result) if not cmd else 'what did you do ?' 
        return ''
    def avail_commands(self):
        comms = ""
        for key in self.cmds.keys():
            comms += "\n\t{}".format(self.cmds[key].descript())
        return comms

    def __str__(self):
        return (f"Shell object for { f'module >=@> {self.mod.name}' if self.mod != 'nomod' else self.mod } \n Available Commands:{ self.avail_commands() }")

    def stop(self):
        self.run = False

    def loop(self):
        self.run = True
        self.shellLoop()
        return True

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

    def set_ifaces(self):
        self.config['ifaces'] = findalldevs()
        self.get_ifaces()

    def get_ifaces(self):
        return self.config['ifaces']

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
        self.config = {}
        self.set_ifaces()




if __name__ == '__main__':
    shell = Shell()
    shell.loop()