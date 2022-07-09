

if __name__ == 'Host':
    from IpAddress import * 
    from MacAddress import * 
else:
    from .IpAddress import * 
    from .MacAddress import * 

class Host:
    
    ip = IpAddress()
    mac = MacAddress()
    network = None
    ports = []
    targeted_ports = []

    def __str__(self):
        return f"HOST OBJECT AT {self.ip if self.ip else ' still an unknown ip address'}"

    def has(self,name=None):
        return hasattr(self,name) and getattr(self,name) is not None if name else name

    def has_port(self):
        True
    def get_port(self,port):
        if self.has_port(port) :True
    
    def register_port(self,port):
        True


    def target_ports(self,ports):
        True

    def set_mac(address):
        self.mac.set_address(address)

    def has_mac(self):
        return self.has('mac')


    def get_mac(self):
        return self.mac if self.has_mac() else self.has_mac()

    def set_ip(self,ip):
        self.ip.set_address(ip)

    def has_ip(self):
        return self.has('ip')


    def get_ip(self):
        return self.ip.get_address() if self.has_ip() else self.has_ip()
    
    def get_targeted_port(self,port):
        matches = self.targeted_ports.filter(lambda a:a.number==port)
        return matches[0] if len(matches) else None  

    def target_port(self,port):
        if get_targeted_port(port) == None:
            self.targeted_ports.append(Port(port))


    def get_ports(self,only_targetted=False):
        return self.targeted_ports if only_targeted is not False  else self.ports


    def __init__(self,ip=None,mac=None):
        if ip : self.set_ip(ip)
        if mac : self.set_mac(mac)

