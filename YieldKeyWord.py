def yieldGenerator():
    yield 1
    yield 2
    yield 3


for value in yieldGenerator():
    print(value)
