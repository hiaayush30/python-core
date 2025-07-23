
class Animal:
    def __init__(self):
        self.age=1
    def eat(self):
        print("eat")

# you can use inheritence or composition
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


fish = Fish()
fish.eat()
print(fish.age)

# every class in python directly or inderictly derives from the object class

print(isinstance(fish,Animal))
print(isinstance(fish,object))

print(issubclass(Fish,Mammal))
     