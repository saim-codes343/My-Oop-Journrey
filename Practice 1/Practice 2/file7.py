from random import *
#Store marks of 15 students
#In each line store roll no followed by marks of Quiz 1 to Quiz 4
#Each quiz has total marks 10  
f = open('marks.txt', 'w')
rno = 1
for i in range(15):
	s = str(rno)+' '+str(randint(0,10))+' '+str(randint(0,10))+' '+str(randint(0,10))+' '+str(randint(0,10))+'\n'
	f.write(s)
	rno += randint(1,2)	#either increment of 1 or 2 in the rollno, showing some roll nos are missing
f.close() 