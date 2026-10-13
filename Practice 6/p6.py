class Matrix3:
  def __init__(self):
    self.elements = [[randint(1,4),randint(1,4),randint(1,4)],[randint(1,4),randint(1,4),randint(1,4)],[randint(1,4),randint(1,4),randint(1,4)]]
  def __str__(self):
    s = ''
    for row in self.elements:
      for element in row:
        s = s + str(element) + ' '
      s = s + '\n'
    return s
  def __add__(self, other):
    result = Matrix3()
    for i in range(3):
      for j in range(3):
        result.elements[i][j] = other.elements[i][j] + self.elements[i][j]
    return result
  
from random import *
m1 = Matrix3()
m2 = Matrix3()
print(m1)
print(m2)
print()
m3 = m1 + m2
print(m3)