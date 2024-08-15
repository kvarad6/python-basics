#reversing string using join and sorted vs using slice
# It first alphabetically sorts the string
# Then reverse the alphabetically sorted string
# So the result is not similar to one getting using slice (string[::-1])


string = "varad"
sortedString = ''.join(sorted(string)) 
reverseSortedString = ''.join(sorted(string, reverse=True)) 
print(sortedString)  # #hiimrs
print(reverseSortedString)

#reversing using slice
string2 = "varad"
print(string2[::-1]) #darav
