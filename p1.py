class Point:
  def about_class():
    print ('This is a class level function')
  def about_object(self):
    print ('This is an object level function')

Point.about_class()
#Point.about_object()
p = Point()
p.about_object()