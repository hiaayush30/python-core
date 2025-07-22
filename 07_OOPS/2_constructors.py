class Point:
    yo="this is class' innate property" # class level attribute
    def __init__(self,x,y):  # self is a reference to the current point object
        self.x= x # these are instance attributes whch are unique to each instance
        self.y= y

    def draw(self): 
        print("drawing on the coordinate",self.x,",",self.y)

    @classmethod
    def zero(cls):  # by convention cls is the name of 1st parameter in a class method which refers to the class itself 
        return cls(0,0)
         


obj = Point(1,2)
print(obj.x)
obj.draw()
obj.z = 32

print(obj.yo)
Point.yo = "property changed"
new_obj = Point(10,20)
print(Point.yo)
print(new_obj.yo) 


new_Point = Point.zero()
print(new_Point.x)