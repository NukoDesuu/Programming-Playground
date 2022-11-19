class Math :
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(x, y):
        return Math(x.a + y.a, x.b + y.b)
    
    def __str__(self):
        return "{0}, {1}".format(self.a, self.b)

class vector : Math

vectorA = Math(25, 35)
vectorB = Math(10, 20)

print(str(vectorA + vectorB))