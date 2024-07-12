# Counting vowels in a given word


word = "programming"

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for character in word:
	if character in vowels:
         count += 1
        
print(count) #--> 3

