#Sort a list of dictionaries by the last name key

people = [
    {"first": "Alice", "last": "Smith"},
    {"first": "Bob", "last": "Johnson"},
    {"first": "Charlie", "last": "Brown"},
]


sortByLastName = lambda person: person["last"]

people.sort(key=sortByLastName)

print(people) #-> [{'first': 'Charlie', 'last': 'Brown'}, {'first': 'Bob', 'last': 'Johnson'}, {'first': 'Alice', 'last': 'Smith'}]
