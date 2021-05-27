class Predicate:

    def __init__(self, name, vars, consts=[], negation=False):
        self.name = name
        self.vars = vars
        self.consts = consts
        self.negation = negation

    def add(self,var):
        self.vars.insert(0,var)

    def add_const(self, const):
        self.consts.insert(0,const)