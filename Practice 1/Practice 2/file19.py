class Record:
	def __init__(self, rno, q1, q2, q3, q4):
		self.rno = rno
		self.q1 = q1
		self.q2 = q2
		self.q3 = q3
		self.q4 = q4
	def __str__(self):
		return (f"   {self.rno:<2}     {self.q1:>2}      {self.q2:>2}      {self.q3:>2}      {self.q4:>2}")

marks = []
f = open('marks.txt', 'r')
s = f.read()
for record in s.strip().split('\n'): #split record on the basis of new line character
	rno, q1, q2, q3, q4 = record.strip().split(' ')	
	marks.append(Record(rno, q1, q2, q3, q4))

print('Roll No Quiz 1  Quiz 2  Quiz 3  Quiz 4')		
for record in marks:
	print (record)
f.close() 