#!/usr/bin/env python3


class Shell:
    
    def setPrompt(self,prompt = '>'):
        self.prompt = prompt
    
    def shellLoop(self):
        while self.run:
            cmd = self.getCmd()
            # print(self.cmds.__contains__(cmd))
            command = self.cmds.get(cmd)
            if command != None:
                if type(command) == type(lambda x:x):
                    command(self)
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

    def getCmd(self):
        return input("{}".format(self.prompt))

    def __init__(self,cmds={},mod='no module'):
        self.run = False
        self.cmds = cmds
        self.mod = mod
        self.setPrompt()





if __name__ == '__main__':
    cmds = {
        'exit':lambda shell : shell.stop(),
        'quit':lambda shell : shell.stop(),
        'pymod':lambda shell,name=5 : print(shell)
    }
    shell = Shell(cmds)
    shell.loop()