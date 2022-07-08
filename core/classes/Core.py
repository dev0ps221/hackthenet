class IpAddress:
    address = None
    hostpart = None
    netpart = None
    def has(self,name=None):
        return hasattr(self,name) and self[name] is not None if name else name
    
    def has_address(self):
        return self.has('address')

    def set_address(self,address=None):
        self.address = address

    def get_address(self):
        return self.address if self.has_address() else self.has_address()



class Host:
    ip = IpAddress()
    ports = []
    targeted_ports = []
    known_ports = []
    
    def get_targeted_port(self,port):
        matches = self.targeted_ports.filter(lambda a:a.number==port)
        return matches[0] if len(matches) else None  

    def target_port(port):
        if get_targeted_port(port) == None:
            self.targeted_ports.append(Port(port))


class Network:

