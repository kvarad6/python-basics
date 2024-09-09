
# Class as a decorator:

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

#----------------------------------------------------------------#

# Usecase of decorator | Using it as timer | tracking the runtime of the function
import time

def timer(originalFunction):
    def wrapper(*args, **kwargs):
        #tracking the start time
        t1 = time.time()
        
        #running the function
        result = originalFunction(*args, **kwargs)
        
        #tracking the end time
        t2 = time.time()
        print("The function {} run for {}".format(originalFunction.__name__, t2-t1)) #The function displayInfo run for 3.8623809814453125e-05
        return result
        
    return wrapper

@timer
def displayInfo(name, age):
    print("I am {} of {} age".format(name, age)) 
    
displayInfo("Bob", 15)


#-------------------------------------------------------------#
#Using multiple decorators

#timer decorator function
import time
def timer(originalFunction):
    def wrapper(*args, **kwargs):
        #tracking the start time
        t1 = time.time()
        
        #running the function
        result = originalFunction(*args, **kwargs)
        
        #tracking the end time
        t2 = time.time()
        print("The function {} run for {}".format(originalFunction.__name__, t2-t1)) #The function displayInfo run for 3.8623809814453125e-05
        return result
        
    return wrapper

#logger decorator function
def logger(originalFunction):
    def wrapper(*args, **kwargs):
        print("{} function is running with the arguments: ({}, {})".format(originalFunction.__name__, *args))
        return originalFunction(*args, **kwargs)
    return wrapper


#calling multiple decorators
@logger
@timer
def displayInfo(name, age):
    print("I am {} of {} age".format(name, age)) 
    
displayInfo("Bob", 15)

"""
Output:
wrapper function is running with the arguments: (Bob, 15)
I am Bob of 15 age
The function displayInfo run for 6.198883056640625e-06
"""

"""
@logger
@timer
def displayInfo(name, age)

can also be written as:
displayInfo = logger(timer(displayInfo("bob", 15)))

so, in case of logger function -> originalFunction is no longer the "displayInfo" but the "wrapper" function returned by the timer function
"""
        
        
