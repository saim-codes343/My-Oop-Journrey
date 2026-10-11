class Point:
  count = 0
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
    Point.count += 1
  def get_count():
    return Point.count
  def __str__(self):
    return 'X: ' + str(self.x) + ', Y: ' + str(self.y)

p0 = Point()
p1 = Point()
p2 = Point (50)
p3 = Point(-50, 50)
print('Point 1: ', p1)
print('Point 2: ', p2)
print('Point 3: ', p3)
if p0 == p1:
  print ('Same')
else:
  print ('Different')
if p2 == p1:
  print ('Same')
else:
  print ('Different')