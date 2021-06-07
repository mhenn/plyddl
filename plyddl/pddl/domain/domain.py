import copy
import itertools
from pddl.domain.types import Type


def _transform_to_action_param(obj, action):
    params = []
    mapping = {}
    obj = list(obj)
    for p in action.parameter:
        instances = []
        for i in p.instances:
            var = obj.pop(0)
            mapping[i] = var
            instances.append(var)
        params.append(Type(instances, p.type))

    return params, mapping


def _get_possible_permutations(params, objects):

    perms = []
    for p in params:
        ln = len(p.instances)
        obj = list(filter(lambda x: x.type == p.type, objects))
        perms.append([e for e in itertools.permutations(obj[0].instances, ln)])

    l = len(perms)
    if l == 1:
        return perms[0]
    t = []
    for i in range(l):
        for j in range(i + 1, l):
            for x in perms[i]:
                for y in perms[j]:
                    t.append(x + y)

    return t


class Domain:

    def __init__(self, name, requirements, types, predicates, actions, functions=None):
        self.name = name
        self.requirements = requirements
        self.predicates = predicates
        self.functions = functions
        self.actions = actions
        self.types = types
        self.grounded_actions = {}

    def ground_actions(self, objects):

        impossible_types = [x for x in objects if x.type not in self.types]
        if len(impossible_types) != 0:
            return False

        for action in self.actions:
            t = _get_possible_permutations(action.parameter, objects)
            self.grounded_actions[action.name] = []
            for el in t:
                ground_action = copy.deepcopy(action)
                typ, mapping = _transform_to_action_param(el, action)
                ground_action.update_params(typ,mapping, objects)
                self.grounded_actions[action.name].append(ground_action)
