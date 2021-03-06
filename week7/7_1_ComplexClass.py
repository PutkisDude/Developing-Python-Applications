#AUTHOR LAURI PUTKONEN
# 1. A complex number is a number that can be expressed in the form a + bi,
# where a and b are real numbers and i is the imaginary unit.
# Create class Complex with attributes, constructors and getters/setters.

class Complex:

    def __init__(self, a, b, i):
        self.a = a
        self.b = b
        self.i = i
    def __str__(self):
        msg = "{}+{}{}".format(self.a, self.b, self.i)
        return msg

    def setA(self,a):
        self.a = a
        
    def getA(self):
        return self.a

    def setB(self,b):
        self.b = b

    def getB(self):
        return self.b

    def setI(self, i):
        self.i = i

    def getI(self):
        return self.i


random = Complex(2,3, 'e')
print(random)

random.setA(5)
random.setB(9)
random.setI('r')
print(random.getA())
print(random)

#OUTPUT:
# 2+3e
# 5
# 5+9r
