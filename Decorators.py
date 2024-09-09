
#Class as a decorator:

class DecoratorClass:
    def __init__(self, originalFunction):
        self.originalFunction = originalFunction
    
    def __call__(self, *args, **kwargs):
        print("__call__ method called this before {}".format(self.originalFunction.__name__))
        return self.originalFunction(*args, **kwargs)

@DecoratorClass
def display():
    print("This is a display function")
    
@DecoratorClass
def displayInfo(name, age):
    print("displayInfo ran with the arguments {} and {}".format(name, age))

display()
#prints: 
# __call__ method called this before display
# This is a display function


displayInfo("bob", 15)
#prints:
# __call__ method called this before displayInfo
# displayInfo ran with the arguments bob and 15
