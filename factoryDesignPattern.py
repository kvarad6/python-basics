#factory design pattern

#parent class
class Animal:
    def speak(self):
        pass
    
#child classes
class Dog:
    def speak(self):
        return "Barking"

class Cat:
    def speak(self):
        return "Meow"
        
#factory class | object will be created in this class
class Factory:
    @staticmethod #as not passing self
    def createAnimal(animalType):
        if animalType == "dog":
            return Dog() #returning object of Dog class
        elif animalType == "cat":
            return Cat() #returning object of Cat class
        else:
            raise ValueError("Unknown Animal")

#creating an object of the factory class
factoryObject = Factory()

#creating object of the dog class by calling method in factory class
dog = factoryObject.createAnimal("dog")
print(type(dog)) #<class '__main__.Dog'>
print(dog) #<__main__.Dog object at 0x79c57c3e6e90>

cat = factoryObject.createAnimal("cat")
print(type(cat)) #<class '__main__.Cat'>
print(cat) #<__main__.Cat object at 0x79c57c726ed0>





            
            
            
            

    
