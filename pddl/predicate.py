from enum import Enum


class Predicate:

    #def __init__(self, name, vars, params, consts=[]):
    def __init__(self, name, params):
        self.name = name
        self.params = params
        #self.vars = vars
        #self.consts = consts
        self.negation = False

    def update_params(self, param):
        for i in range(len(self.params)):
            p = self.params[i]
            if p in param:
                self.params[i] = param[p]


    def add(self, var):
        self.vars.insert(0, var)

    def add_const(self, const):
        self.consts.insert(0, const)


class GroupType(Enum):
    AND = 0
    OR = 1
    FORALL = 2
    EXISTS = 3
    WHEN = 4
    NUMERIC = 5


class PredicateGroup:

    def __init__(self, type, predicate):
        self.type = type
        self.predicate = predicate
        pass

    def update_params(self, params):
        pred = self.predicate
        if type(pred) == list:
            for p in pred:
                p.update_params(params)
        else:
            self.predicate.update_params(params)


class QuantifyGroup(PredicateGroup):

    def __init__(self, type, predicate, params):
        super().__init__(type, predicate)
        self.params = params


class ConditionGroup(PredicateGroup):

    def __init__(self, type, predicate, antecedent):
        super().__init__(type, predicate)
        self.antecedent = antecedent


class NumericGroup(PredicateGroup):

    def __init__(self, type, predicate, operator, value):
        super().__init__(type, predicate)
        self.operator = operator
        self.value = value
        self.negation = False

