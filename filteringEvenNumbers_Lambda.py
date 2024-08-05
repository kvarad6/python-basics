#Create a list of even numbers from another list
#(Filtering even numbers)

numbers = [1,2,3,4,5]

evenList = lambda x:x%2==0

filteredList = list(filter(evenList, numbers))

print(filteredList)
