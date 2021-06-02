import itertools


class Domain:

    def __init__(self, name, requirements, types, predicates, actions, functions=None):
        self.name = name
        self.requirements = requirements
        self.predicates = predicates
        self.functions = functions
        self.actions = actions
        self.types = types

    def _get_possible_permutations(self, params, objects):

        perms = []
        for p in params:
            ln = len(p.instances)
            obj = list(filter(lambda x: x.type == p.type, objects))
            perms.append( [e for e in itertools.permutations(obj[0].instances, ln)])

        l = len(perms)
        if l == 1:
            return perms
        t = []
        for i in range(l):
            for j in range(i+1,l):
                for x in perms[i]:
                    for y in perms[j]:
                        t.append(x+y)

        return t


    def _set_predicate_vars(self, ):
        pass


    def ground_actions(self, objects):

        impossible_types = [ x for x in objects if x.type not in self.types]
        if len(impossible_types) != 0:
            return False

        for action in self.actions:
            t = self._get_possible_permutations(action.parameter, objects)
            print(t)