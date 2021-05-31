from pddlyacc import parser


def read_file(name):
    f = open('./res/' + name, 'r')
    data = f.readlines()
    f.close()
    return ''.join(data)


data = read_file('test.pddl')
#data = read_file('pacman_domain.pddl')

domain = parser.parse(data)
print(domain)