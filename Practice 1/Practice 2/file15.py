#read marks and just print on screen
f = open('marks.txt', 'r')
s = f.read()
for record in s.strip().split('\n'): #split record on the basis of new line character
	for elements in record.strip().split(' '): #split each value on the basis of space character
		print (elements, end = ' ')
	print()
f.close() 