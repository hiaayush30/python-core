class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y

    def draw(self): 
        print("drawing on the coordinate",self.x,",",self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self,other):   # Python will automatically figure out the smaller than method now
        return self.x > other.x and self.y>other.y


obj1 = Point(10,20)
obj2 = Point(1,2)

print(obj1==obj2)  # False

print(obj1.__eq__(obj2))
print(obj1 > obj2) 