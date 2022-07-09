
from socket import *
from os import getcwd
from sys import path
import netifaces
import scapy

#We make sur to avoid import issues | #nous prenons soin d'eviter les erreurs d'importation
insert = path.insert
here = '/'.join(__file__.split('/')[:-1])
insert(0, here+'/../classes')
if __name__ == '__main__':
    from Module import *
else:
    from core.classes.Module import *


class Portscandev (Module):




    def simple_scan(self,module,tgt=None,ports=None):

        def _do(ports=None):
            tgt = None
            print(self.actual_target)
            if self.actual_target[1] :
                tgt = self.actual_target[1]
            else:
                while tgt == None :                
                    gottgt = self.shell.get_ip('simplescan>')
                    tgt = self.shell.process_target(gottgt if self.shell.valid_ip(gottgt) or self.shell.valid_network(gottgt) else None)
                self.add_target(tgt)
            openPorts = []
            openports = 0
            while tgt:
                closedports = []
                filteredports = []
                TGT = tgt.get_ip()
                MINPORT = self.shell.get_port('simplescan>','\t\t\t\t\tgive me the minimum port to check')
                MAXPORT = self.shell.get_port('simplescan>','\t\t\t\t\tgive me the maximum port to check')
                try:
                        if(gethostbyname(TGT)):
                                pg = 0
                                arr = (range(MINPORT,MAXPORT+1))  if (MINPORT < MAXPORT > MINPORT) else [MINPORT]
                                for port in arr:
                                        system('clear')
                                        print(f"running portscan against {gethostbyname(TGT)}:[{MAXPORT-MINPORT if MINPORT < MAXPORT > MINPORT else MINPORT}] ports on TCP FLOW")
                                        pg += 1
                                        print(f'progress : {pg}/{MAXPORT-(MINPORT if (MINPORT < MAXPORT > MINPORT) else len([MINPORT]))}',end='\r')
                                        try:
                                                conn = create_connection((TGT,port),timeout=5)
                                                print(conn)
                                                if conn:
                                                    openPorts.append(port)
                                                    openports+=1
                                                else:
                                                    filteredports.append(port)
                                                conn.close()
                                        except Exception as e:
                                                closedports.append(port)
                                                print(f'\n encountered errors -> .{e} for port :{port}')
                                print('',end='\n')
                                system('clear')
                                print('scan results')
                                [print(f'\t - port {openPorts[p]} is open') for p in openports]
                                [print(f'\t - port {p} is open|filtered') for p in filteredports]
                                print(f'\t - {len(closedports)} closed ports')
                                
                        else:
                                print('the specified host address is wrong or the host is not up !!')
                except Exception as e:
                        print('the specified host address is wrong or the host is not up !!')
                tgt = self.next_target()
            self.next_target()
        try:
            while True:
                _do(ports)
        except KeyboardInterrupt as e:
            print('closing...')

    def help(self):
        return f"""
    MODULE {self.name}
        """

    def __init__(self,name='portscan'):
        Module.__init__(self,name)
        self.register_action(
            'simplescan',self.simple_scan
        )



if __name__ == '__main__':
    d = Portscan()
    d.shell.loop()
