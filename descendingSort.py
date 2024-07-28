# Sort a list in descending without using list.sort

# approach 1 | using new list | extra space
originalList = [2,1,5,4,3]
newList = []

while originalList:
    minimum = originalList[0]
    for num in originalList:
        if minimum<num:
            minimum = num
    newList.append(minimum)
    originalList.remove(minimum)
        
print(newList)
    
    
