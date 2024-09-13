# "The Sky is Blue" -> "Blue is the Sky"

#-------- Approach 1 --------#
#Converting original string to list -> reverse the list -> convert reversed list to string
originalString = "The Sky is Blue"
#step1: converting original string to list using .split()
wordList = originalString.split()

#step2: reverse the list using slice
reversedList = wordList[::-1]

#step3: convert the reversed list back to the string
reversedString = " ".join(reversedList)
print(reversedString)
    
