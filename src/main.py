from pddlyacc import parser


def read_file(name):
    f = open('./res/' + name, 'r')
    data = f.readlines()
    f.close()
    return ''.join(data)


#data = read_file('test.pddl')
#data_dom = read_file('pacman/domain.pddl')
#data_prob = read_file('pacman/pb0.pddl')

data_dom = read_file('/blocksworld/domain.pddl')
data_prob = read_file('/blocksworld/pb.pddl')

domain = parser.parse(data_dom)
problem = parser.parse(data_prob)
print(domain.ground_actions(problem.objects))
print('asd')