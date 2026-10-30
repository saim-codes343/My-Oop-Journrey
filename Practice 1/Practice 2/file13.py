lst = []
f = open('num_random.txt', 'r')
s = f.read()
sum = 0
for value in s.split(' '):
	if value == '':  #to handle the last empty element
		break
	lst.append(int(value))
f.close() 
print(lst)
lst.sort()
print(lst)