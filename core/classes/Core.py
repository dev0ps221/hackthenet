
if __name__ == 'Core':
    from Host import *
    from IpAddress import *
    from MacAddress import *
    from Port import *
    from Network import *
else :
    from .Host import *
    from .IpAddress import *
    from .MacAddress import *
    from .Port import *
    from .Network import *