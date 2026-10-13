class Matrix2:
    def __init__(self,a,b,c,d):
        self.elements = [[a,b],[c,d]]

    def __str__(self):
        result = ''
        for row in self.elements:
            for elements in row:
                result = result + str(elements) + ' '
            result = result + '\n'
        return result

m = Matrix2(1, 2, 3, 4)
print(m)