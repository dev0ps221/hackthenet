#!/usr/bin/env python3

from sys import path

#We make sur to avoid import issues | #nous prenons soin d'eviter les erreurs d'importation
insert = path.insert
here = '/'.join(__file__.split('/')[:-1])
insert(0, here+'/../classes')
if __name__ == '__main__':
    from Module import *
    from Shell import *
else:
    from core.classes.Module import *
    from core.classes.Shell import *

class TheShell(Module):
    def help(self):
        return f"""
    MODULE {self.name}
        """

    def __str__(self):
        return 'nomod'

    def __init__(self,name='nomod'):
        Module.__init__(self,name)
        self.shell = Shell(mod=self)
        self.shell.loop() 
        globals()['shell'] = self