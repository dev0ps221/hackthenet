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
        True

    def get_local_ifaces(self):
        True

    def local(self,arg):
        if arg in 'ips':
            return self.get_local_ips()

        if arg in 'ifaces':
            return self.get_local_ifaces()


    def help(self):
        return f"""
    MODULE {self.name}
        """

    def register_actions(self):
        register_action(
            'local',self.local
        )

    def __init__(self,name='discover'):
        Module.__init__(self,name)



if __name__ == '__main__':
    d = Discover()
    d.shell.loop()
