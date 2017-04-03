from random import choice

list_ = open("text.txt").read().split()

n = 100

restr=[choice(list_) for i in range(n)]

print(' '.join(restr))
