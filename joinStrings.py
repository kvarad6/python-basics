#.join() keyword uses in case of tuple, list and dict
#usecase : Converting list into string

myTuple = ("John", "Peter", "Vicky")
myList = ["John", "Peter", "Vicky"]
myDict = {"user1":"John", "user2":"Peter", "user3":"Vicky"}

seperator = "#"

x = seperator.join(myTuple)
y = seperator.join(myList)
zKey = seperator.join(myDict)
zValue = seperator.join(myDict.values())

print(x) #--> John#Peter#Vicky
print(y) #--> John#Peter#Vicky
print(zKey) #--> user1#user2#user3
print(zValue) #--> John#Peter#Vicky
