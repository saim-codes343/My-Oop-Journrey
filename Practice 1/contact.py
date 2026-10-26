class Contact:
    def __init__(self, fname, sname, desig, salary):
        self.fname = fname
        self.sname = sname
        self.desig = desig
        self.salary = salary

    def getFname(self):
        return self.fname

    def getSname(self):
        return self.sname

    def getDesig(self):
        return self.desig

    def getSalary(self):
        return self.salary

    def setFname(self, fname):
        self.fname = fname

    def setSname(self, sname):
        self.sname = sname

    def setDesig(self, desig):
        self.desig = desig

    def setSalary(self, salary):
        self.salary = salary

    def getContact(self):
        name = f'{self.fname} {self.sname}'
        return f'{name:<20}\t{self.desig:<15}\t{self.salary:>8}'

    def __str__(self):
        return self.getContact()
