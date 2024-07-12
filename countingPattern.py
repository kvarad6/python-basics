
# Counting Digits, Letters, and Spaces in a String | using regex

import re

str = 'Python is 1'

#pattern to match digits
print(len(re.findall("\d", str))) #--> 1
#-----(or)------#
print(len(re.findall("[0-9]", str))) #--> 1

#matching letters
print(len(re.findall("[a-zA-Z]", str))) #--> 8


#matching spaces
print(len(re.findall("\s", str))) #--> 2
