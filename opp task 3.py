class Recetangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  
print("Area of rectangle is:",Recetangle(5,10).area())
print("Area of rectangle is:",Recetangle(7,3).area())      