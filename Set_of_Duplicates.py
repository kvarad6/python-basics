# Program to print set of duplicates in a list

lst = [1,2,3,3,4,5,6,6]

#------- Approach 1 ---------#
#more concise way
print(set([num for num in lst if lst.count(num)>1]))

#----- Approach 2 -------#
#more readble way | using counter (from collections)

from collections import Counter

count = Counter(lst)
print(count)  #-> Counter({3: 2, 6: 2, 1: 1, 2: 1, 4: 1, 5: 1})
print(count.items()) #-> dict_items([(1, 1), (2, 1), (3, 2), (4, 1), (5, 1), (6, 2)])

print(set(num for num, count in count.items() if count>1)) #-> {3, 6}
