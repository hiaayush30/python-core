class Employee:
    def greet(self):
        print("Employee greet")
class Person:
    def greet(self):
        print("Person greet")

class Manager(Employee,Person):
    pass  

m = Manager();
m.greet()