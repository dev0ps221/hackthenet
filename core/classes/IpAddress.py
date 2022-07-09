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