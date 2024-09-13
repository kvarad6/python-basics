#finding max repeated chars in string

testString = "varadAND"
#modify the string
testString = testString.lower()

#need to store the frequency of each character in the dict
freqDict = {}

for char in testString:
    if char in freqDict:
        freqDict[char] += 1
    else:
        freqDict[char] = 1

#finding the max frequency, and using that frequency, finding the char having that frequency

maxFrequency = max(freqDict.values())

for char, freq in freqDict.items():
    if freq == maxFrequency:
        print(char)

