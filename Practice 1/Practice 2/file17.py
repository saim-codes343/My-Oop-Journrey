#read marks and just print on screen
f = open('marks.txt', 'r')
s = f.read()
print('Roll No Quiz 1  Quiz 2  Quiz 3  Quiz 4')		
for record in s.strip().split('\n'): #split record on the basis of new line character
	rno, q1, q2, q3, q4 = record.strip().split(' ')		 #split each value on the basis of space character
	print (rno, q1, q2, q3, q4)
f.close() 