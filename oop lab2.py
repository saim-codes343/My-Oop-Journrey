class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")

    def __del__(self):
        print(f"Object {self.name} destroyed.")

A = Demo("A")
print("Deleting Object.")
del A
print("End of program")