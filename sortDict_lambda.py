#sorting a list of dicts by "last" key

people = [
    {"first": "Alice", "last": "Smith"},
    {"first": "Bob", "last": "Johnson"},
    {"first": "Charlie", "last": "Brown"},
]

#-------- Appraoch 1 ---------#

sortByLastName = lambda person: person["last"]

people.sort(key=sortByLastName)

#can also be written as:
people.sort(key = lambda person: person["last"])

print(people) #-> [{'first': 'Charlie', 'last': 'Brown'}, {'first': 'Bob', 'last': 'Johnson'}, {'first': 'Alice', 'last': 'Smith'}]


#------ Approach 2 ------#
sortedList = sorted(people, key= lambda person: person["last"])

print(sortedList) #-> [{'first': 'Charlie', 'last': 'Brown'}, {'first': 'Bob', 'last': 'Johnson'}, {'first': 'Alice', 'last': 'Smith'}]


