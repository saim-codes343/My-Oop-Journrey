f = open('abc.txt', 'r')
s = f.read()
for line in s.split('\n'):
	print(line)
f.close() 