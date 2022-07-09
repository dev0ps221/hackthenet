from scapy.all import Net


if (__name__ == 'Network'):
    from Host import * 
else:
    from .Host import * 

class Network:
    hosts = []
    targeted_hosts = []

    def get_hosts(self,only_targetted=False):
        return self.targeted_hosts if only_targeted else self.hosts

    def __init__(self,netrange=""):
        print(netrange)
        hosts = [Host(host) for host in Net(netrange)]
        [print(host) for host in self.get_hosts()]


