# Program to extract digits from a given string

#---------- Approach 1 ----------#
strnum = "1r3h4kjs4hj2w"

nums = ""

# method 1:
for char in strnum:
    if char.isdigit() is True:
        nums += char

print(nums)

#method 2:
#also can be solved using join, filter and lambda | pending

#-------- Approach 2 ---------#
testString = "wef2342dwe"

import re

result = re.findall('\d', testString)

print(result)

#------- Approach 3 ---------#
testString = "wef2342dwe"

resultList = filter(str.isdigit, testString)
print("".join(resultList)) #2342


