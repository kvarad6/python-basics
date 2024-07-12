
# Adding Two List Elements Together


list1 = [1,2,3,4]
list2 = [5,6,7,8]

list3 = []

for i in range(0, len(list1)):
	list3.append(list1[i] + list2[i])
    
print(list3) #--> [6, 8, 10, 12]
