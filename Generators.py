# Generators don't hold entire result in memory, it yields one result at a time.

# normal list | without using yield keyword:

def squareNumbers(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result


squaredNums = squareNumbers([1, 2, 3, 4, 5])

print("squaredNums: ", squaredNums)
# output: squaredNums:  [1, 4, 9, 16, 25]

# ------------------------------------------------------------

# using "yield" keyword -> normal function becomes generator


def squareNumbers(nums):
    for num in nums:
        yield(num*num)


squaredNums = squareNumbers([1, 2, 3, 4, 5])

print("squaredNums: ", squaredNums)
# output: squaredNums:  <generator object squareNumbers at 0x10278deb0>

print("next(squaredNums):", next(squaredNums))  # 1
print("next(squaredNums):", next(squaredNums))  # 4
print("next(squaredNums):", next(squaredNums))  # 9
print("next(squaredNums):", next(squaredNums))  # 16
print("next(squaredNums):", next(squaredNums))  # 25
print("next(squaredNums):", next(squaredNums))  # StopIteration exception


for num in squaredNums:
    print(num)
    # output: 1 4 9 16 25

# --------------------------------------------------------------

# same example using list comprehension:


