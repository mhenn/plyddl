
class Domain:

    def __init__(self, name, requirements, types, predicates, actions):
        self.name = name
        self.requirements = requirements
        self.predicates = predicates
        self.actions = actions
        self.types = types
