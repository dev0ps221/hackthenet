from os import getcwd
from sys import path
insert = path.insert
  
insert(0, getcwd()+'/../classes')
from Module import *



class Discover (Module):
    def __init__(self,name):
        Module.__init__(self,name='discover')



if __name__ == '__main__':
    d = Discover()
    d.shell.loop()
