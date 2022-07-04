class Module:


    actions = {}

    def runAction(self,func):
        def action(*args):
            return func(self,*args)
        return action

    def register_action(self,name,func):
        self.actions[name] = self.runAction(func)

    def __init__(self,name):
        self.name = name

