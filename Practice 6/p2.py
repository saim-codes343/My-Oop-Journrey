class Matrix3:
  def __init__(self):
    self.elements =[[randint(1,4),randint(1,4),randint(1,4)],[randint(1,4),randint(1,4),randint(1,4)],[randint(1,4),randint(1,4),randint(1,4)]]
  def __str__(self):
    s = ''
    for row in self.elements:
      for element in row:
        s = s + str(element) + ' '
      s = s + '\n'
    return s

from random import *
m = Matrix3()
print(m)