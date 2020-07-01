class vector2:
    #init vector
    def __init__(self, e0, e1):
        self.e = [e0, e1]
    
    def __add__(self, other):
        return vector2(self.e[0] + other.e[0], self.e[1] + other.e[1])
    
    def __sub__(self, other):
        return vector2(self.e[0] - other.e[0], self.e[1] - other.e[1])
    
    def __mul__(self, other):
        return 

point2 = vector2