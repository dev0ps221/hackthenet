from os import getcwd
__import__(f'..',globals(),locals())
__import__(f'..',globals(),locals())
__import__(f'..',globals(),locals())



class Discover(Module):


    def initialize_actions(self):
        self.register_action(
            'add_commande',lambda self,name,action:self.shell.add_commande(name,action)
        )

    def set_shell_commands(self):
        def show(command,self,arg):
            print(command,self,arg)
            if arg:
                print('asked to show ',arg)
        self.runAction(
            'add_commande','show',show
        )

    def initialize_shell(self):
        self.shell = Shell({},self)

    def __init__(self,name):
        Module.__init__(self,name)
        self.initialize_shell()
        self.initialize_actions()
        
d = Discover()
Discover.shell.getCmd('show').run()