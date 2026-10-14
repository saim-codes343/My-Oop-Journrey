class Matrix2:
    def __init__(self, a, b):
        self.a, self.b = a
        self.c, self.d = b
    def __str__(self):
        return f"Matrix:\n{self.a} {self.b}\n{self.c} {self.d}"
m= Matrix2([1,2],[3,4])
print(m)

        