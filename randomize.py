
# Randomizing the Items of a List

from random import shuffle

lst = ['Python', 'is', 'Easy']

# print(lst.shuffle()) #--> AttributeError: 'list' object has no attribute 'shuffle'

print(shuffle(lst)) #--> None

print(lst) #--> ['Easy', 'Python', 'is']
