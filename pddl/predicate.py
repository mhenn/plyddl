from enum import Enum


class Predicate:

    def __init__(self, name, vars, consts=[]):
        self.name = name
        self.vars = vars
        self.consts = consts
        self.negation = False
        self.type = type

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


class QuantifyGroup(PredicateGroup):

    def __init__(self, type, predicate, params):
        super().__init__( type, predicate)
        self.params = params


class ConditionGroup(PredicateGroup):

    def __init__(self, type, predicate, antecedent):
        super().__init__( type, predicate)
        self.antecedent = antecedent


class NumericGroup(PredicateGroup):

    def __init__(self, type, predicate, operator, value):
        super().__init__(type,predicate)
        self.operator =operator
        self.value = value
        self.negation = False

