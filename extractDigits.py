# Program to extract digits from a given string

strnum = "1r3h4kjs4hj2w"

nums = ""

# method 1:
for char in strnum:
    if char.isdigit() is True:
        nums += char

print(nums)

#method 2:
#also can be solved using join, filter and lambda | pending
