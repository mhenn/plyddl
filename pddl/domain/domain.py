
class Domain:

    def __init__(self, name, requirements, types, predicates, actions, functions=None):
        self.name = name
        self.requirements = requirements
        self.predicates = predicates
        self.functions = functions
        self.actions = actions
        self.types = types
