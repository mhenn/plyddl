
class Domain:

    def __init__(self, name, requirements, predicates, actions):
        self.name = name
        self.requirements = requirements
        self.predicates = predicates
        self.actions = actions
        self.types = []
