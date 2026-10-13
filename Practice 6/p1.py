class Employee:
  def __init__(self, name):
    self.name = name
    self.skills = ['Sales','Marketing','Accounts']
  def __str__(self):
    return 'Name: ' + self.name + '\n' + 'Skills: ' + str(self.skills)

from copy import *
e1 = Employee('Amjad')
e2 = copy(e1)
e2.name = 'Sajid'
#print (e1)
#print (e2)
e1.skills.append('Communicaiton')
#print (e1)
#print (e2)
e3 = deepcopy(e2)
e3.skills.append('Fazool Skill')
print (e2)
print (e3)