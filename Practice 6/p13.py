class Matrix2:
    def __init__(self, a, b, c, d):
        self.elements = [[a, b], [c, d]]

    def __str__(self):
        result = ''
        for row in self.elements:
            for value in row:
                result = result + str(value) + ' '
            result = result + '\n'
        return result

    def __add__(self, other):
        a = self.elements[0][0] + other.elements[0][0]
        b = self.elements[0][1] + other.elements[0][1]
        c = self.elements[1][0] + other.elements[1][0]
        d = self.elements[1][1] + other.elements[1][1]
        return Matrix2(a, b, c, d)

    def __eq__(self, other):
        return self.elements == other.elements


m1 = Matrix2(1, 2, 3, 4)
m2 = Matrix2(5, 6, 7, 8)
m3 = m1 + m2
print(m3)
print(m1)
print(m2)
if m3 == Matrix2(6, 8, 10, 12):
    print('Same')
else:
    print('Different')

if m1 == m2:
    print('Same')
else:
    print('Different')