from os import getcwd
from sys import path
insert = path.insert
here = '/'.join(__file__.split('/')[:-1])

insert(0, here+'/../classes')

if __name__ == '__main__':
    from Module import *
else:
    from core.classes.Module import *


class Discover (Module):
    def __init__(self,name='discover'):
        Module.__init__(self,name)



if __name__ == '__main__':
    d = Discover()
    d.shell.loop()
