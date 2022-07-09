

if __name__ == 'Host':
    from IpAddress import * 
    from Port import * 
    from MacAddress import * 
else:
    from .IpAddress import * 
    from .Port import * 
    from .MacAddress import * 

class Host:
    
    ip = None
    mac = MacAddress()
    network = None
    ports = []
    targeted_ports = []

    def __str__(self):
        return f"HOST OBJECT AT {self.ip if self.ip else ' still an unknown ip address'}"

    def has(self,name=None):
        return hasattr(self,name) and getattr(self,name) is not None if name else name

    def has_port(self,port):
        match = None
        for p in self.ports:
            if p.get_number() == port : match = p.get_number() == port 
        return match
    
    def get_port(self,port):
        match = None
        for p in self.ports:
            if p.get_number() == port : match = p
        return match
    
    def register_port(self,port):
        if not self.has_port(port) : self.ports.append(Port(port,self.ip))


    def target_ports(self,ports):
        for port in ports : self.target_port(port) 

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
        matches = [e for e in filter(lambda a:a.get_number()==port if a else a,self.targeted_ports)]
        return matches[0] if len(matches) else None  

    def target_port(self,port):
        if not self.has_port(port):
            self.register_port(port)
        if self.get_targeted_port(port) == None:
            self.targeted_ports.append(self.get_port(port))

    def get_ports(self,only_targeted=False):
        return self.targeted_ports if only_targeted is not False  else self.ports

    def register_open_port(self,port):
        if self.has_port(port):
            self.register_port(port)
        self.get_port(port).switch_status('open')
        if self.get_targeted_port(port) is not None:
            self.get_targeted_port(port).switch_status('open')

    def register_closed_port(self,port):
        if not self.has_port(port):
            self.register_port(port)
        self.get_port(port).switch_status('closed')
        if self.get_targeted_port(port) is not None:
            self.get_targeted_port(port).switch_status('closed')

    def register_filtered_port(self,port):
        if not self.has_port(port):
            self.register_port(port)
        self.get_port(port).switch_status('filtered')
        if self.get_targeted_port(port) is not None:
            self.get_targeted_port(port).switch_status('filtered')

    def register_unknown_port(self,port):
        if not self.has_port(port):
            self.register_port(port)
        self.get_port(port).switch_status('unknown')
        if self.get_targeted_port(port) is not None:
            self.get_targeted_port(port).switch_status('unknown')


    def __init__(self,ip=None,mac=None):
        if ip : 
            self.ip = IpAddress(ip)
        if mac : self.set_mac(mac)

