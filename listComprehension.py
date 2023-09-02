
import time
# list comprehension vs for loop

# using for loop..

charList = []

for char in 'character list':
    charList.append(char)

print("charList:", charList)
# output: charList: ['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', ' ', 'l', 'i', 's', 't']

# using list comprehension..
charListComp = [char for char in 'character list']
print("charListComp:", charListComp)
# output: charListComp: ['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', ' ', 'l', 'i', 's', 't']

# ------------------------------------

# time analysis | list comprehension vs for loop

resultList = []


def expoFun(num):
    for i in range(num):
        resultList.append(i**2)
    return resultList


begin = time.time()
expoFun(10**6)
end = time.time()

print("time taken by for loop:", round(end-begin, 2))


def compreFun(n):
    return [i**2 for i in range(n)]


begin = time.time()
compreFun(10**6)
end = time.time()
print("time taken by comprehension:", round(end-begin, 2))
