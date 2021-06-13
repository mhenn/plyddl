from plyddl.pddl.predicate import Predicate

class SimpleAction:

    def __init__(self,name):
        self.name = name;
        self.effect_pos = []
        self.effect_neg = []
        self.precond = []
        self.params = []

class Node:

    def __init__(self):
        self.path = []
        self.state = []
        self.acts = []


def get_pos_neg_effects_simple(effects):

    dic = {'pos':[], 'neg':[]}

    for effect in effects.predicate:
        eff =str(effect)
        if eff[:3:] == 'not':
            dic['neg'].append(eff[3::])
        else:
            dic['pos'].append(eff)
    return dic

def get_actions_simple(ground):
    actions = []

    for tag in ground:
        for action in ground[tag]:
            a = SimpleAction(tag)
            if isinstance(action.precondition[0], Predicate):
                a.precond = str(action.precondition[0])
            else:
                a.precond = [ str(pre) for pre in action.precondition[0].predicate]
            a.params = action.parameter
            dic = get_pos_neg_effects_simple(action.effects[0])
            a.effect_pos = dic['pos']
            a.effect_neg = dic['neg']
            actions.append(a)

    return actions


def goal_init(problem):
    goal = [str(g) for g in problem.goal[0].predicate]
    init = [str(p) for p in problem.init[0].predicate]
    return goal, init


def mergeSets(s1, s2):
    l = list(s1) + list(s2)
    return set(l)


def removeEffects(target, effects):
    for effect in effects:
        target.discard(effect)
    return target


def contains(o, l):
    return next((True for x in l if x.state == o.state), False)


def get_fulfillable_actions(ground, state):
    actions = [a for a in ground if set(a.precond).issubset(set(state))]
    return actions


def progression_planning(iniState, goals, ground):
    startNode = Node()
    startNode.state = iniState
    startNode.actions = get_fulfillable_actions(ground, iniState)
    queue = [startNode]
    # goals = set(map(tuplize,dp.goals()))
    explored = []
    i = 0
    while len(queue) > 0:
        node = queue[0]
        queue = queue[1:]
        explored.append(node)

        for act in node.actions:
            child = Node()
            child.state = mergeSets(node.state, act.effect_pos)
            child.state = removeEffects(child.state, act.effect_neg)

            if not contains(child, explored):
                if not contains(child, queue):
                    child.actions = get_fulfillable_actions(ground, child.state)

                    child.path = node.path.copy()
                    child.path.append(act)

                    if goals.issubset(set(child.state)):
                        return child.path
                    queue.append(child)
