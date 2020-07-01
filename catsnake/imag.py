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
        
        #add complex with imaginary
        if type(other) == "imag":
            imag = self.imag + other.val
            return comp(self.real, imag)

        #add complex with real
        else:
            real = self.real + other
            return comp(real, self.imag)
    
    def __sub__(self, other):
        #subtract complex
        if type(other) == "comp":
            real = self.real - other.real
            imag = self.imag - other.imag
            return comp(real, imag)
        else:
            real = self.real - other
            return comp(real, self.imag)


class imag:
    #initialize imaginary number
    def __init__(self, value):
        self.val = value
    
    #add
    def __add__(self, other):
        #imag + imag
        if type(other) == "imag":
            #return imag
            return imag(self.val + other.val)
        #imag + comp
        if type(other) == "comp":
            #return complex
            return comp(other.real, other.imag + self.val)
        #imag + real
        else:
            #return complex
            return comp(other, self.val)
    
    def __sub__(self, other):
        if type(other) == "imag":
            return imag(self.val - other.val)
        
        if type(other) == "comp":
            return comp(other.real, self.val - other.imag)
    
        else:
            return comp(-other.real, self.val - other.imag)