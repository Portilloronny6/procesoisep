class Triangulo():

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        area = pow(s * (s - self.__a) * (s - self.__b) * (s - self.__c), 0.5)
        return area


triangulo = Triangulo(2, 4, 3)
area = triangulo.area()
print(area)
