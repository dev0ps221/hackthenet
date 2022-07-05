from os import getcwd
from sys import path
import socket
import netifaces


#We make sur to avoid import issues | #nous prenons soin d'eviter les erreurs d'importation
insert = path.insert
here = '/'.join(__file__.split('/')[:-1])
insert(0, here+'/../classes')
if __name__ == '__main__':
    from Module import *
else:
    from core.classes.Module import *


class Discover (Module):


    def get_local_ips(self):
        return 'requested get local ips'

    def get_local_ifaces(self):
        return 'requested get local ifaces'

    def local(self,module,arg=None):
        if arg:
            if arg in 'ips':
                return self.get_local_ips()

            if arg in 'ifaces':
                return self.get_local_ifaces()
        else:
            def get_targetted():
                print('what do you want to discover')
                print('choose between :\n  ips\n  ifaces\n  exit')
                return input(f'{self.shell.prompt}@local>')
            run = True
            while run:
                arg = get_targetted()
                cmd,args = self.shell.parseInput(arg)
                if arg in 'ips':
                    res = self.shell.process_results({'name':f'local {cmd}'},self.get_local_ips())
                elif arg in 'ifaces':
                    res = self.shell.process_results({'name':f'local {cmd}'},self.get_local_ifaces())
                elif arg == 'exit':
                    return False
                else:
                    res = self.shell.process_cmd(cmd,*args)
            return res


    def help(self):
        return f"""
    MODULE {self.name}
        """

    def register_actions(self):
        self.register_action(
            'local',self.local
        )

    def __init__(self,name='discover'):
        Module.__init__(self,name)
        self.register_actions()



if __name__ == '__main__':
    d = Discover()
    d.shell.loop()
