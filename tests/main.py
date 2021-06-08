from src.parse import Plyddl

p = Plyddl()

def read_file(name):
    f = open('./res/' + name, 'r')
    data = f.readlines()
    f.close()
    return ''.join(data)


#data = read_file('test.pddl')
domain = 'pacman/domain.pddl'
pb = 'pacman/pb0.pddl'

#domain = '/blocksworld/domain.pddl'
#pb = '/blocksworld/pb.pddl'

p.parse(domain,pb)
p.ground()
print('asd')