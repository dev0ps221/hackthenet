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

    ifaddresses = {}
    def get_local_ips(self):
        ifaddrs = [(iface,[(ifelem,netifaces.ifaddresses(iface)[ifelem]) for ifelem in netifaces.ifaddresses(iface)]) for iface in self.get_local_ifaces()]
        
        for (iface,data) in ifaddrs:
            self.ifaddresses[iface] = {}
            for (key,val) in data: 
                self.ifaddresses[iface][key] = val
        ret = []
        for iface in self.ifaddresses:
            retdata='\n\t'+f'{iface}:'
            for data in self.ifaddresses[iface]:
                retdata+='\n\t\t'+f'{data} : {self.ifaddresses[iface][data]}'
            ret.append(retdata) 
            self.update_ip_addresses()
        return ret
    def update_ip_addresses(self):
        print([*filter(lambda x : x == 2,self.ifaddresses.keys())])
    def get_local_ifaces(self):
        return netifaces.interfaces()

    def local(self,module,arg=None):
        if arg:
            if arg in 'ips':
                return self.shell.process_results({'name':f'local {arg}'},self.get_local_ips(),True)

            if arg in 'ifaces':
                return self.shell.process_results({'name':f'local {arg}'},self.get_local_ifaces(),True)
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
                    res = self.shell.process_results({'name':f'local {cmd}'},self.get_local_ips(),True)
                elif arg in 'ifaces':
                    res = self.shell.process_results({'name':f'local {cmd}'},self.get_local_ifaces(),True)
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
