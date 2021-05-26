class Action:

    def __init__(self, parameter, precondition, effects):
        self.parameter = parameter
        self.precondition = precondition
        self.effects = effects


class Parameter:

    def __init__(self, vars):
        self.vars = vars


class Precondition:

    def __init__(self, predicate, vars, negation=False):
        self.predicate = predicate
        self.vars = vars
        self.negation = negation


class Effect:

    def __init__(self, predicate, vars):
        self.predicate = predicate
        self.vars = vars
