from abc import ABC, abstractclassmethod

class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(controls):         # polymorphism
    for control in controls:
        control.draw()

ddl = DropDownList()  
textbox = TextBox()  
print(isinstance(ddl,UIControl))
draw([ddl,textbox])