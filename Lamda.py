# Lamda -> Function without a name | Anonymous functions

# Any no. of arguments | one expression

# def defined function vs lamda functions

def cubeFun(y):
    return y*y*y


print("def defined fun output:", cubeFun(3))

lamdaCubeFun = lambda y : y*y*y

print("lamda function output:", lamdaCubeFun(3))

# -----------------------------------------------

max = lambda a,b: a if a>b else b
print(max(2,3))

# ------------

# lamda with filter...
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print("adults:", adults)
# -----------------------

# lambda | map()

# Multiply all elements of a list by 2 using lambda and map() function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

modifiedList = list(map(lambda x: x*2, li))
print("modifiedList: ", modifiedList)

#-------------------------------------------

# Transform all elements of a list to upper case using lambda and map() function

animals = ['dog', 'cat', 'parrot', 'rabbit']
upperAnimalList = list(map(lambda animal: animal.upper(), animals))

print("upperAnimalList: ", upperAnimalList)

#-----------------------------------------



