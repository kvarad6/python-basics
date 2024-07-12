# Writing fibonnaci series
# fib[-1] --> accessing last index element
# fib[-2] --> accessing second last index element

fib = [0,1]

for i in range(5):
	fib.append(fib[-1]+fib[-2])
    
print(fib) #--> [0, 1, 1, 2, 3, 5, 8]


#converting above list of integers to string

strFib = []

for num in fib:
	strFib.append(str(num))
    
print(",".join(strFib)) #--> 0,1,1,2,3,5,8
	
