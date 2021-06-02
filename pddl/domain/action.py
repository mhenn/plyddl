class Action:

    def __init__(self,name, parameter, precondition, effects):
        self.name = name
        self.parameter = parameter
        self.precondition = precondition
        self.effects = effects
        self.ground = []

class Precondition:

    def __init__(self, predicate, vars, negation=False):
        self.predicate = predicate
        self.vars = vars
        self.negation = negation


class Effect:

    def __init__(self, predicate, vars):
        self.predicate = predicate
        self.vars = vars
