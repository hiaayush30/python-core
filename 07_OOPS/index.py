# Class: blueprint for creting new objects
# Object : instance of a class

class Point:
    def draw(self):  # all fns should have atleast 1 parameter and by convention we call it self
        print("draw")


obj = Point()
print(type(obj))
print(isinstance(obj,int))
print(isinstance(obj,Point))
obj.draw()