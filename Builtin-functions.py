# Python Built-in Functions

# abs() -> 	Returns the absolute value of a number

x = abs(-1.25)
print(x) #1.25

y = abs(3+5j)
print(y) # 5.830951894845301

#---------------------------------#

# all() -> returns True if all items in an iterable are true, otherwise it returns False
# If the iterable object is empty, the all() function also returns True.


myList = [1, 1, 0]
print(all(myList)) #False

myTuple = (0, True, False)
print(all(myTuple)) #False

mySet = {1, 0, 1}
print(all(mySet)) #False

# When used on a dictionary, the all() function checks if all the keys are true, not the values
myDict = {1: "Pune", 0: "Mumbai"}
print(all(myDict)) #False

#--------------------------------------#

#any() -> Returns True if any item in an iterable object is true
# If the iterable object is empty, the any() function will return False.

myList = [1, 1, 0]
print(any(myList)) #True

myTuple = (0, 1, False)
print(any(myTuple)) #True

mySet = {1, 0, 1}
print(any(mySet)) #True

# When used on a dictionary, the any() function checks if any of the keys are true, not the values
myDict = {1: "Pune", 0:"Mumbai"}
print(any(myDict)) #True

#--------------------------------------#

#ascii() -> Returns a readable version of an object. Replaces none-ascii characters with escape character

x = ascii("My name is Ståle भारत")
print(x)
# 'My name is St\xe5le \u092d\u093e\u0930\u0924'
# å -> \xe5
# भारत -> \u092d\u093e\u0930\u0924

#-------------------------------------#

#bin() -> Returns the binary version of a number

x = bin(25)
print(x) # 0b11001
# The result will always have the prefix 0b

#--------------------------------------------#

#bool() -> Returns the boolean value of the specified object
#The object will always return True, unless:
    #The object is empty, like [], (), {}
    #The object is False
    #The object is 0
    #The object is None

print(bool(1)) #True
print(bool(0)) #False
print(bool([])) #False
print(bool(None)) #False

#---------------------------#

#bytearray() -> Returns an array of bytes

x = bytearray(4)
print(x) # bytearray(b'\x00\x00\x00\x00')

# syntax: bytearray(x, encoding, error)
# if x (source) -> int -> empty bytearray object of the specified size will be created
# if x (source) -> string -> Need to specify the encoding of the source.

# errror -> Specifies what to do if the encoding fails.

#------------------------------#







