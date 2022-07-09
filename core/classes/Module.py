
from colorama import Fore, Back, Style
if __name__ == 'Module':
    from Shell import *
else:
    from core.classes.Shell import *
    
class Module:


    actual_target = (-1,None)
    actions = {}

    def help(self):
        return f"""
    MODULE {self.name}
        """


    def setPrompt(self,prompt = 'hackthenet>'):
        self.shell.setPrompt(f"{Style.RESET_ALL+Style.BRIGHT+Back.BLACK+Fore.RED+' '+self.name+Back.BLACK+Fore.GREEN+'> '+Style.RESET_ALL if self.name != 'nomod' else ''}{Back.RED}{prompt} {Style.RESET_ALL}")


    def setAction(self,func):
        def action(*args):
            return func(self,*args)
        return action

    def runAction(self,name,*args):
        action = self.get_action(name)
        if action != None and callable(action) :
            return action(*args)
        else:
            return action


    def get_action(self,name):
        return self.actions[name] if self.has_action(name) else None 

    def has_action(self,name):
        return name in self.actions

    def register_action(self,name,func):
        self.actions[name] = self.setAction(func)


    def _targets(self):
        return self.config['targets']


    def add_target(self,target):
        self.config['targets'].append(target)
        self.shell.add_target(target)
        print(f'appended target {target}')
        self.actual_target = (-1,None)
        self.next_target()

    def remove_target(self,target):
        self.config['targets'] = []
        for tgt in self._targets:
            self.add_target(tgt) if tgt != target else None

        self.shell.remove_target(target)
        return self._targets()


    def initialize_actions(self):
        self.register_action(
            'add_commande',lambda name,action:self.shell.add_commande(name,action)
        )
        self.set_shell_commands()

    def set_shell_commands(self):
        def show(command,arg=None):
            print(command,self,arg)
            if arg:
                ret = self.config[arg] if arg in self.config else self.shell.config[arg] if arg in self.shell.config else "No match found"
                print()
                return ''.join([str(e) for e in ret]) if type(ret) is list else str(ret)
        self.register_action(
            'show',show
        )

    def set_config(self,name,val):
        self.config[name] = val
        self.shell.set_config(name,val)

    def get_configs(self):
        return []

    def get_config(self,name):
        try:
            return self.config[name] if self.config[name] else self.shell.get_config()
        except:
            return self.shell.get_config()

    def unset_config(self,name):
        try:
            del(self.config[name])
            self.config[name] = None
            self.shell.unset_config(name)
            return True
        except:
            return False


    def initialize_shell(self):
        self.shell = Shell({},self)
        self.shell_prompt = self.shell.prompt
        self.setPrompt(self.shell_prompt)
        self.shell.initCmds()

    def next_target(self):
        idx,target = self.actual_target
        targets_size = len(self._targets())
        if targets_size:
            if idx >=0 and idx < targets_size:
                idx+=1
                self.actual_target = idx,self._targets()[idx]
            else  :
                self.actual_target = -1,None
        else  :
            self.actual_target = -1,None
        return self.actual_target[1]


    def get_actual_target(self):
        return self._targets()[self.actual_target[0]] if self.actual_target[0] >= 0 else None


    def __init__(self,name,config={'targets':[]}):
        self.name = name
        self.config = config
        self.initialize_shell()
        self.initialize_actions()
        self.next_target()
        self.config['actual_target'] = self.actual_target


