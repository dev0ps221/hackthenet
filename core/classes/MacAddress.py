

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
