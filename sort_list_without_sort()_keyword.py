

#sorting the list using selection sort
lst = [3,2,1,5,4]
n = len(lst)

for i in range(0, n):
    minIndex = i
    for j in range(i+1, n):
        if lst[j]<lst[minIndex]:
            minIndex = j
            
    lst[i], lst[minIndex] = lst[minIndex], lst[i]

print(lst)
        
        
#sorting the list using bubble sort
lst = [3,2,1,5,4]
n = len(lst)

for i in range(0,n):
    for j in range(0, n-i-1):
        if lst[j]>lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            
print(lst)
