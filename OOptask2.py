class Demo:
    def __init__(self,name):
        self.name = name
        print(f"Object {self.name} created.")

    def __del__(self):
        print(f"Object {self.name} destroyed.")

obj1 = Demo("A")
obj2 = Demo("B")
obj3 = obj1
obj4 = obj3
print("obj1 removed")
del obj1
print("obj2 removed")
del obj2
print("obj3 removed")
del obj3
print("obj4 removed")
del obj4
