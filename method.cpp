#methods implementation

class Dog:
    def __init__(self, name, breed):
	    self.name = name
	    self.breed = breed
    def bark(self):
    	print(f"{self.name} barks")
    

#creating an object of the class "Dog"
myDog = Dog("sheru", "local")

#calling the method using object.method
myDog.bark()
