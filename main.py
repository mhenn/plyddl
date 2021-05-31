from pddlyacc import parser


def read_file(name):
    f = open('./res/' + name, 'r')
    data = f.readlines()
    f.close()
    return ''.join(data)


#data = read_file('test.pddl')
#data = read_file('pacman/domain.pddl')
data = read_file('pacman/pb0.pddl')

#data = read_file('/blocksworld/domain.pddl')
#data = read_file('/blocksworld/pb.pddl')

domain = parser.parse(data)
print(domain)