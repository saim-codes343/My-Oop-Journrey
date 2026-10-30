from random import *
f = open('num_random.txt', 'w')
for i in range(10):
	f.write(str(randint(0, 100))+' ')
f.close() 