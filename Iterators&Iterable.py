nums = [1, 2, 3]

print(dir(nums))
#output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# contains __iter__ method, so loopover is possible if this method is present.
# So, list is iterable, but not a iterator.

print(next(nums))
# output: TypeError: 'list' object is not an iterator
# that's why, list is not iterator as it doesn't have __next__ method.

# Iterator of nums list:
i_nums = iter(nums)         # alternate of -> nums.__iter__()
print("i_nums: ", i_nums)

print("dir: ", dir(i_nums))
# it has both __iter__ and __next__ method, so, it's an iterator
# Iterators are also iterables (__iter__ method)

print("next: ", next(i_nums))   # 1
print("next: ", next(i_nums))   # 2
print("next: ", next(i_nums))   # 3
print("next: ", next(i_nums))   # StopIteration
