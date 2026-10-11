class Point:
    
    def about_object(self): 
        print('This is an object level function') 
#Point.about_object() # is an error 
p = Point() 
p.about_object() # works 
Point.about_object(p) # works 
