num=10

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break;
else:
    print("prime")


#to check if number is prime or not

#---------- Approach 1 ---------#
#prime no-> divible by only 1 and itself and has only 2 divisors
#TC: O(n)
#SC: O(1)
n = 5

count = 0

for i in range(1, n+1):
    if n%i == 0:
        count += 1

if count == 2:
    print("the number is prime")
else:
    print("the number is not a prime")

#-------- Approach 2 ---------#

#no need to calculate till n, just calculate till n//2
#or we can also achieve the same by calculating till squareroot of n
n = 10
count = 0

for i in range(2, (n//2)+1):
    if n%i == 0:
        print("the number is not a prime")
        break
else:
    print("the number is a prime number")
    
