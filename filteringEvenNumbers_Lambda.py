#Create a list of even numbers from another list
#(Filtering even numbers)

numbers = [1,2,3,4,5]

evenList = lambda x:x%2==0

filteredList = list(filter(evenList, numbers))

print(filteredList)


#filtering even list | create a list of even numbers from another list

#-------- Approach 1 ---------#
lst = [1,2,3,4,5,6]
evenLst = []

for num in lst:
    if num%2==0:
        evenLst.append(num)
print(evenLst)

#-------- Approach 2 ----------#
using filter

testLst = [1,2,3,4,5,6]

def checkEven(num):
    if num%2==0:
        return True
    else:
        return False

evenList = []

filterFunction = filter(checkEven, testLst)

for obj in filterFunction:
    print(obj)
    
#------- Approach 3 --------#

testLst = [1,2,3,4,5,6]

checkEven = lambda num: num%2==0

evenList = []

filterFunction = filter(checkEven, testLst)
filteredList = list(filterFunction)
print(filteredList)


