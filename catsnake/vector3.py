import math

class vector3:
    def __init__(self, e1, e2, e3):
        self.e = [e1, e2, e3]
    #vector3 + vector3
    def __add__(self, other):
        return vector3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])
    #vector3 - vector3
    def __sub__(self, other):
        return vector3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])
    #vector3 * other
    def __mul__(self, other):
        #vector3 * vector3
        if isinstance(other, vector3):
            return vector3(self.e[0] * other.e[0], self.e[1] * other. e[1], self.e[2] * other.e[2])
        #vector3 * num
        else:
            return vector3(self.e[0] * other, self.e[1] * other, self.e[2] * other)
    #vector3 / other
    def __truediv__(self, other):
        #vector3 / vector3
        if isinstance(other, vector3):
            return vector3(self.e[0]/other.e[0], self.e[1]/other.e[1], self.e[2]/other.e[2])
        #vector3 / num
        else:
            return self * (1 / other)
    
    def length_squared(self):
        return sum(k ** 2 for k in self.e)

    def length(self):
        return math.sqrt(self.length_squared())

    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]

    r = x
    g = y
    b = z

point3 = vector3
color = vector3
