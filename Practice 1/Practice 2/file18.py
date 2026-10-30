#read marks and just print on screen
f = open('marks.txt', 'r')
s = f.read()
print('Roll No Quiz 1  Quiz 2  Quiz 3  Quiz 4')		
for record in s.strip().split('\n'): #split record on the basis of new line character
	rno, q1, q2, q3, q4 = record.strip().split(' ')	
	#use f-string to align the columns
	print (f"   {rno:<2}     {q1:>2}      {q2:>2}      {q3:>2}      {q4:>2}")	
f.close()