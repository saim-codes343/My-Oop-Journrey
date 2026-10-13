class Matrix3:
  def __init__(self, name):
    self.name = name
    self.elements = [[randint(1,4),randint(1,4),randint(1,4)],[randint(1,4),randint(1,4),randint(1,4)],[randint(1,4),randint(1,4),randint(1,4)]]
  def __str__(self):
    s = ''
    for row in self.elements:
      for element in row:
        s = s + str(element) + ' '
      s = s + '\n'
    #print ("Length of S:" , len(s))
    return s
  def __add__(self, other):
    result = Matrix3('Result')
    for i in range(3):
      for j in range(3):
        result.elements[i][j] = other.elements[i][j] + self.elements[i][j]
    return result
  def __del__(self):
    print (self.name, ' is going to die')

from random import *
m1 = Matrix3('M1')
m2 = Matrix3('M2')
print(m1)
print(m2)
print(m1 + m2)