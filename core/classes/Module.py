
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
        self.shell.setPrompt(f"{self.name+'@' if self.name != 'nomod' else ''}{prompt}")


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


    def remove_target(self,target):
        self.config['targets'] = []
        for tgt in self._targets:
            self.add_target(tgt) if tgt != target else None
        return self._targets()


    def initialize_actions(self):
        self.register_action(
            'add_commande',lambda self,name,action:self.shell.add_commande(name,action)
        )

    def set_shell_commands(self):
        def show(command,self,arg):
            if arg:
                print('asked to show ',arg)
        self.register_action(
            'show',show
        )

    def initialize_shell(self):
        self.shell = Shell({},self)
        self.shell_prompt = self.shell.prompt
        self.setPrompt(self.shell_prompt)

    def next_target(self):
        idx,target = self.actual_target
        targets_size = len(self._targets())
        idx+=1
        if idx < targets_size :
            self.actual_target = idx,self._targets()[idx]
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


