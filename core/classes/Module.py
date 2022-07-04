class Module:


    actions = {}

    def runAction(func):
        def action(*args):
            return func(self,*args)
        return action

    def register_action(name,func):
        self.actions[name] = self.runAction(func)

    def __init__(self,name):
        self.name = name