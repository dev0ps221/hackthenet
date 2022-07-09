from scapy.all import Net


if (__name__ == 'Network'):
    from Host import * 
else:
    from .Host import * 

print(Host)
class Network:
    hosts = []
    targeted_hosts = []

    def get_hosts(self,only_targeted=False):
        return self.targeted_hosts if only_targeted else self.hosts

    def __init__(self,netrange=""):
        for host in Net(netrange):
            hostObject = Host(host)
            self.hosts.append(hostObject)


