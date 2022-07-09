class IpAddress:
    address = None
    hostpart = None
    netpart = None
    def has(self,name=None):
        return (hasattr(self,name) and getattr(self,name) is not None) if name else name
    
    def has_address(self):
        return self.has('address')

    def set_address(self,address=None):
        self.address = address

    def __str__(self):
        return f" IPADDRESS:{self.address} "

    def get_address(self):
        return self.address if self.has_address() else self.has_address()

    def __init__(self,ip=None):
        if ip: self.set_address(ip)

class MacAddress:
    address = None
    def has(self,name=None):
        return hasattr(self,name) and getattr(self,name) is not None if name else name
    
    def __str__(self):
        return f" MACADDRESS:{self.address} "

    def has_address(self):
        return self.has('address')

    def set_address(self,address=None):
        self.address = address

    def get_address(self):
        return self.address if self.has_address() else self.has_address()

    def __init__(self,mac=None):
        if mac: self.set_address(mac)

class Port:
    number = None
    ip = None
    status = 'unknown'

    def has(self,name=None):
        return hasattr(self,name) and getattr(self,name) is not None if name else name

    def set_number(port):
        self.number = port

    def has_number(self):
        return self.has('number')


    def get_number(self):
        return self.number if self.has_number() else self.has_number()

    def set_ip(self,port):
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

class Network:
    hosts = []
    targeted_hosts = []
    

    def __init__(self,netrange=[]):
        print(netrange)


class Host:
    ip = IpAddress()
    mac = MacAddress()
    network = Network()
    ports = []
    targeted_ports = []

    def __str__(self):
        return f"HOST OBJECT AT {self.ip if self.ip else ' still an unknown ip address'}"

    def has(self,name=None):
        return hasattr(self,name) and getattr(self,name) is not None if name else name

    def has_port(self):

    def get_port(self,port):
        if self.has_port(port)
    
    def register_port(self,port):
        


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

    def __init__(self,ip=None,mac=None):
        if ip : self.set_ip(ip)
        if mac : self.set_mac(mac)

