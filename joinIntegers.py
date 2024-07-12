
# .join() for integer list


#------- Approach 1 ---------#

myIntList = [1,2,3,4,5]

strRep = ",".join(str(num) for num in myIntList)

print(strRep) #--> 1,2,3,4,5


#------ Approach 2 ----------#

# convert int list to str list, then apply join

myNumList = [1,2,3,4,5]

seperator = ","

strList = []

for num in myNumList:
	strList.append(str(num))
    
    
print(",".join(strList)) #--> 1,2,3,4,5
