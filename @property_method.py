class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    #property decorator creates a property object named getRadius.
    @property
    def getRadius(self):
        return self._radius
    
    #The getRadius here refers to the property object created by @property.
    #.setter is a method of the property object that designates the following function as the setter for this property.
    @getRadius.setter
    def setRadius(self, value):
        if value<0:
            print("Radius can't be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14 * self._radius
        
circleObj = Circle(2)
print(circleObj.getRadius) #2
circleObj.setRadius = 3
print(circleObj.getRadius) #3
print(circleObj.area) #9.42
