from scapy.all import Net


if (__name__ == 'Network'):
    from Host import * 
else:
    from .Host import * 

class Network:
    hosts = []
    targeted_hosts = []

    def get_active_hosts(self):
        return [host for host in filter(lambda host:host.isUp(),self.get_hosts())]


    def get_hosts(self,only_targeted=False):
        return self.targeted_hosts if only_targeted is not False else self.hosts

    def __init__(self,netrange=""):
        self.hosts = []
        for host in [e for e in Net(netrange)]:
            hst = str(host)
            hostObject = Host(hst)
            self.hosts.append(hostObject)


