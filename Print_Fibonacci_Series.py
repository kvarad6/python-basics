# Write a program to print fibonacci series
def fiboSeries(n: int):
	if n<=0:
	    return 0
	elif n==1:
	    return 1
	return fiboSeries(n-1)+fiboSeries(n-2)
    
n=10
for i in range(0,n):
    print(fiboSeries(i))
    
	
