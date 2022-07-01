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
                
    def stop(self):
        self.run = False

    def loop(self):
        self.run = True
        self.shellLoop()

    def getCmd(self):
        return input("{}".format(self.prompt))

    def __init__(self,cmds={}):
        self.run = False
        self.cmds = cmds
        self.setPrompt()





if __name__ == '__main__':
    cmds = {
        'exit':lambda shell : shell.stop(),
        'quit':lambda shell : shell.stop(),
        'pymod':lambda shell,name=5 : print(shell)
    }
    shell = Shell(cmds)
    shell.loop()