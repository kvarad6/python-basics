# Counting consonants in a given word
# consonants --> those which are not vowels

word = "programming"

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for character in word:
	if character not in vowels:
         count += 1
        
print(count) #--> 8

