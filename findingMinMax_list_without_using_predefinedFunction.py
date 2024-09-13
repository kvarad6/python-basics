lst = [1,2,3,4,5]

minValue = lst[0]
maxValue = lst[0]

for num in lst:
    if num<minValue:
        minValue = num
    if num>maxValue:
        maxValue = num
    
print("minValue:", minValue)
print("maxValue:", maxValue)
