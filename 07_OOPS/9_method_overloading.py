# method overririding means replacing or extending a method defined in the base class
# here we can replace(by default) or extend (using super) the __init__ method in Animal via __init__ in Mammal class
class Animal:
    def __init__(self):
        print("Animal constructor called")
        self.age=1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor called")
        self.weight=2
        super().__init__()

    def walk(self):
        print("walk")

 
m = Mammal()
print(f"age:{m.age},weight:{m.weight}")