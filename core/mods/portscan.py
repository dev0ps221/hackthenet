
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


class Portscan (Module):



    def run(self,module,tgt=None,ports=None):

        def _do(ports=None):
            self.last_results.append([])
            tgt = None
            if self.actual_target[1] :
                tgt = self.actual_target[1]
            else:
                while tgt == None :                
                    gottgt = self.shell.get_ip('>')
                    tgt = self.shell.process_target(gottgt if self.shell.valid_ip(gottgt) or self.shell.valid_network(gottgt) else None)
                    
                self.add_target(tgt)
            tgt = self.get_actual_target()
            def process_tgt(tgt,MINPORT,MAXPORT):
                openPorts = []
                openports = 0
                if tgt.get_ip() and tgt.get_ip().split('.')[-1] not in ['255','0']:
                    closedports = []
                    filteredports = []
                    TGT = tgt.get_ip()
                    try:
                            if(gethostbyname(TGT)):
                                    tgt.target_ports(range(MINPORT,MAXPORT+1))
                                    pg = 0
                                    arr = tgt.get_ports(True)
                                    for port in arr:
                                            port = port.get_number()
                                            system('clear')
                                            print(f"running portscan against {gethostbyname(TGT)}:[{MAXPORT-MINPORT if MINPORT < MAXPORT > MINPORT else MINPORT}] ports on TCP FLOW")
                                            pg += 1
                                            print(f'progress : {pg}/{MAXPORT-(MINPORT if (MINPORT < MAXPORT > MINPORT) else len([MINPORT]))}',end='\r')
                                            try:
                                                    conn = create_connection((TGT,port),timeout=5)
                                                    if conn:
                                                        tgt.register_open_port(port)
                                                        conn.close()
                                            except timeout as e:
                                                    tgt.register_filtered_port(port)
                                            except ConnectionRefusedError as e:
                                                    tgt.register_closed_port(port)
                                                    print(f'\n encountered errors -> .{e} for port :{port}')
                                    print('',end='\n')
                            else:
                                    print(TGT,'mmmm')
                                    print('the specified host address is wrong or the host is not up !!')
                    except Exception as e:
                        print(e)
            while tgt is not None:
                if type(tgt) is Host:
                    MINPORT = self.shell.get_port('>','\t\t\t\t\tgive me the minimum port to check')
                    MAXPORT = self.shell.get_port('>','\t\t\t\t\tgive me the maximum port to check')
                    process_tgt(tgt,MINPORT,MAXPORT)
                    self.last_results[-1].append(f'results for {tgt.get_ip()}')
                    [self.last_results[-1].append('\t'+str(p.get_number())+' is open')  for p in filter(lambda p: p.status == 'open' if p else None,tgt.get_ports(True))]
                if type(tgt) is Network:
                    MINPORT = self.shell.get_port('>','\t\t\t\t\tgive me the minimum port to check')
                    MAXPORT = self.shell.get_port('>','\t\t\t\t\tgive me the maximum port to check')
                    
                    for t in tgt.get_hosts():
                        process_tgt(t,MINPORT,MAXPORT)
                    for tgt in tgt.get_hosts():
                        self.last_results[-1].append(f'results for {tgt.get_ip()}')
                        [self.last_results[-1].append('\t'+str(p.get_number())+' is open')  for p in filter(lambda p: p.status == 'open' if p else None,tgt.get_ports(True))]
                tgt = self.next_target()
            self.next_target()
        try:
            _do(ports)
            self.results()
        except KeyboardInterrupt as e:
            print('closing...')


    def help(self):
        return f"""
    MODULE {self.name}
        """

    def __init__(self,name='portscan'):
        Module.__init__(self,name)



if __name__ == '__main__':
    d = Portscan()
    d.shell.loop()
