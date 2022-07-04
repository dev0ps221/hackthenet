class Module:


    actions = {}

    def runAction(self,func):
        def action(*args):
            return func(self,*args)
        return action

    def register_action(self,name,func):
        self.actions[name] = self.runAction(func)

    def _targets(self):
        return self.config['targets']

    def add_target(self,target):
        self.config['targets'].append(target)

    def __init__(self,name,config={targets:[]}):
        self.name = name
        self.config = config
        
