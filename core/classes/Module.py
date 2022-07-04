class Module:


    actual_target = (-1,None)
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
    
    def remove_target(self,target):
        self.config['targets'] = []
        for tgt in self._targets:
            self.add_target(tgt) if tgt != target
        return self._targets()

    def next_target(self):
        idx,target = self.actual_target
        targets_size = len(self._targets)
        idx+=1
        if idx < targets_size :
            self.actual_target = idx,self._targets()[idx]
        else  
            self.actual_target = -1,None
        return self.actual_target[1]

    def __init__(self,name,config={targets:[]}):
        self.name = name
        self.config = config
        
