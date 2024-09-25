# Builder Design Pattern

#Base Class
class Car:
    def __init__(self):
        self.color = None
        self.engine = None
        self.seats = None
        
    def __str__(self):
        return "Color is {}, Engine is {}, Seats are {}".format(self.color, self.engine, self.seats)

#Builder Class | to create an object of the base class step by step
class Builder:
    #initialising an object of the base class
    def __init__(self):
        self.car = Car()
    
    #modifying the object step by step
    def setColor(self, color):
        self.car.color = color
        return self
    
    def setEngine(self, engine):
        self.car.engine = engine
        return self
    
    def setSeats(self, seats):
        self.car.seats = seats
        return self

    #finally, a build method to build the object with the properties
    def build(self):
        print("the car has been built completely")
        return self.car
        
#initialising an object of the builder class
buildObj = Builder()

#modifying the object of the base class using the builder class
sportsCar = buildObj.setColor("red").setEngine("V8").setSeats(4).build()
print(sportsCar) #Color is red, Engine is V8, Seats are 4

