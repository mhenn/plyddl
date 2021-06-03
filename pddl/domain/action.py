from pddl.domain.types import Type


class Action:

    def __init__(self, name, parameter, precondition, effects):
        self.name = name
        self.parameter = parameter
        self.precondition = precondition
        self.effects = effects

    def update_params(self, param_type, param_mapping):
        self.parameter = param_type
        for p in self.precondition:
            p.update_params(param_mapping)
        for e in self.effects:
            e.update_params(param_mapping)

