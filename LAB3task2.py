class Students:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def set(self,n,r,m):
        self.name = n
        self.rollno = r
        self.marks = m
    def printData(self):
        print("Name", self.name)
        print("Roll NO", self.rollno)
        print("Marks", self.marks)


s1=Students("Ali",101,85.5)
s1.printData()
print("After setting new data" )
s1.set("Sara",102,91.3)
s1.printData()



