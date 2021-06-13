from plyddl.parse import Plyddl
from planning import *

p = Plyddl()

#data = read_file('test.pddl')
#domain = 'pacman/domain.pddl'
#pb = 'pacman/pb0.pddl'

domain = '/blocksworld/domain.pddl'
pb = '/blocksworld/pb.pddl'

p.parse(domain, pb)
p.ground()
a = get_actions_simple(p.domain.grounded_actions)
g = goal_init(p.problem)
pat = progression_planning(g[1], set(g[0]), a)
print([p.name for p in pat])

print('asd')