class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

obj1 = Point(10,20)
obj2 = Point(1,2)

print((obj1+obj2).x) 