class Predicate:

    def __init__(self, name, vars, negation=False):
        self.name = name
        self.vars = vars
        self.negation = negation

    def add(self,var):
        self.vars.append(var)