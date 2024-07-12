
# Comparing Two Strings for Anagrams

# anagram --> rearranging words results into same


str1 = "Listen"

str2 = "Silent"

str1 = list(str1.upper())
str2 = list(str2.upper())

str1.sort()
str2.sort()

if str1==str2:
	print("Strings are anagrams")
else:
	print("Strings are not anagrams")


