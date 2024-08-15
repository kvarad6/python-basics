# *args (Non-Keyword Arguments) -> can be considered as a dictionary that maps each keyword to the value that we pass alongside it
# **kwargs (Keyword Arguments) -> used to pass a keyworded, variable-length argument list.

# -> used when we have doubts about the number of arguments we should pass in a function.

# *args
def multiArg(*args):
    for argv in args:
        print(argv)

multiArg("abc", "xyz")

#------------------------

# **kwargs

def multiKwargs(**kwargs):
    for key, value in kwargs.items():
        print(key,value)


multiKwargs(first="geek", second="for", third="geeks", forth="website")

#-------------------------------

# *args and **kwargs in a single function..

def combiFunction(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ("firstArg", "secondArg", "thirdArg")
combiFunction(*args)

kwargs = {"firstArg":"firstArg", "secondArg":"secondArg", "thirdArg":"thirdArg"}
combiFunction(**kwargs)

#----------------------------------
#Example:
#*args, **kwargs

def randomName(*args, **kwargs):
    print(args)
    print(kwargs)
    if "role" in kwargs:
        print(f"{kwargs['role']} is my role")
    
randomName((1,2,3,4, 5), name="varad", surname="kulkarni", role="software engineer")


