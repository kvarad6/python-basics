#__call__ method

class Multiplier:
    #init method
    def __init__(self, factor):
        self.factor = factor
    
    #call method
    def __call__(self, x):
        return x*self.factor

#creating an object of the class Multiplier
double = Multiplier(2)

#using an object as a function, __call__ method comes into the picture
result = double(5)
print(result) #10

triple = Multiplier(3)
print(triple(5)) #15
