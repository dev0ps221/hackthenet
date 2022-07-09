from os import getcwd
from sys import path
import socket
import netifaces
from scapy.all import get_if_list,get_if_addr,get_working_if


#We make sur to avoid import issues | #nous prenons soin d'eviter les erreurs d'importation
insert = path.insert
here = '/'.join(__file__.split('/')[:-1])
insert(0, here+'/../classes')
if __name__ == '__main__':
    from Module import *
else:
    from core.classes.Module import *


class Iface:
    def __init__(self,name,data):
        self.name = name
        self.data = data


class Discover (Module):

    ifaddresses = {}
    def get_local_ips(self):
        ifaddrs = [(iface,{f"{iface}",get_if_addr(iface)}) for iface in self.get_local_ifaces()]
        
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
        print([*filter(lambda x : x == '2',self.ifaddresses.keys())])
    def get_local_ifaces(self):
        return get_if_list()

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

    def network(self,arg):

        

        def get_targetted():
            print('which network do you want to discover ?\n[type a network representation]\n\tex : 192.168.1.1/24\t[type enter for a local network discovery]')
            return self.shell.getCmd(f'@network>')
        netrep = get_targetted()
        netrep = netrep if netrep != "" else gateways()['default'][AF_INET][0] 
        print(self.shell.valid_network(netrep))


    def help(self):
        return f"""
    MODULE {self.name}
        """

    def register_actions(self):
        self.register_action(
            'local',self.local
        )
        self.register_action(
            'network',self.network
        )

    def __init__(self,name='discover'):
        Module.__init__(self,name)
        self.register_actions()



if __name__ == '__main__':
    d = Discover()
    d.shell.loop()
