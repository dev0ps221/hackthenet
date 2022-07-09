
class Port:
    number = None
    ip = None
    status = 'unknown'

    def switch_status(self,status):
        if status in ['open','closed','filtered','unknown']:
            self.status = status

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
