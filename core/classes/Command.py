#!/usr/bin/env
class Command:


    def descript(self):
        ret = (self.name)
        ret+=(f"\t{self.desc if self.desc else 'AUCUNE DESCRIPTION ACTUELLEMENT DISPONIBLE'}")
        return ret

    def help(self):
        print(self.descript())
        print(self.show_usage())
    
    def show_usage(self):
        ret = ('Utilisation')
        ret+=(f"\t{self.usage if self.usage else 'NON DOCUMENTÉ !!'}")
        return ret

    

    def run(self,*args):
        return self.action(self,*args) if len(args) else self.action(self)

    def __init__(self,name,func,desc=None,usage=None):
        self.name = name 
        self.desc = desc
        self.usage = usage
        self.action = func


