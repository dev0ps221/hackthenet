class IpAddress:
    address = None
    hostpart = None
    netpart = None
    def has(self,name=None):
        return (hasattr(self,name) and self[name] is not None) if name else name
    
    def has_address(self):
        return self.has('address')

    def set_address(self,address=None):
        self.address = address

    def get_address(self):
        return self.address if self.has_address() else self.has_address()

class MacAddress:
    address = None
    def has(self,name=None):
        return hasattr(self,name) and self[name] is not None if name else name
    
    def has_address(self):
        return self.has('address')

    def set_address(self,address=None):
        self.address = address

    def get_address(self):
        return self.address if self.has_address() else self.has_address()

class Port:
    number = None
    ip = None
    def has(self,name=None):
        return hasattr(self,name) and self[name] is not None if name else name

    def set_number(port):
        self.number = port

    def has_number(self):
        return self.has('number')


    def get_number(self):
        return self.number if self.has_number() else self.has_number()

    def set_ip(port):
        self.ip = port

    def has_ip(self):
        return self.has('ip')


    def get_ip(self):
        return self.ip if self.has_ip() else self.has_ip()

    def __init__(self,port=None,ip=None):
        if port:
            set_number(port)
        if ip:
            set_ip(ip)

class Host:
    ip = IpAddress()
    mac = MacAddress()
    network = Network()
    ports = []
    targeted_ports = []
    known_ports = []

    def has(self,name=None):
        return hasattr(self,name) and self[name] is not None if name else name
    
    def get_targeted_port(self,port):
        matches = self.targeted_ports.filter(lambda a:a.number==port)
        return matches[0] if len(matches) else None  

    def target_port(port):
        if get_targeted_port(port) == None:
            self.targeted_ports.append(Port(port))


class Network:
    hosts = []
    targeted_hosts = []


