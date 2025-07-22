# __init__ and __str__ are examples of magic methods
class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y

    def draw(self): 
        print("drawing on the coordinate",self.x,",",self.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"



obj = Point(1,2)
print(obj) # gives module name, class name and memory address of the object by default