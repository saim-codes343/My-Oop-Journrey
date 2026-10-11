class Point:
  count = 0
  def __init__(self, x, y):
    self.x = x
    self.y = y
    Point.count += 1
  def get_count():
    return Point.count

print('Count: ', Point.get_count())
p1 = Point (50,100)
p2 = Point(-50, 50)
print('Count: ', Point.get_count())
