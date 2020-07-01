class comp:
    #init complex number
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    #add 2 complex numbers
    def __add__(self, other):
        #add complex with other complex
        if type(other) == "comp":
            real = self.real + other.real
            imag = self.imag + other.imag
            return comp(real, imag)
        #add complex with other complex
        else:
            real = self.real + other
            return comp(real, self.imag)


class imag:
    def __init__(self, value):
        self.val = value
    
    def __add__(self, other):
        if type(other) == "imag":
            return imag(self.val + other.val)
        
        if type(other) == "comp":
            return comp(other.real, other.imag + self.val)
        
        else:
            return comp(other, self.val)
    
    def __sub__(self, other):
        if type(other) == "imag":
            return imag(self.val - other.val)
        
        if type(other) == "comp":
            return comp(other.real, self.val - other.imag)
    
        else:
            return comp(-other.real, self.val - other.imag)