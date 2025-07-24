class Text(str):
    def duplicate(self): # self here is an instance of the string class ie a string itself
        return self +" "+ self


text = Text("PyThON");
print(text.duplicate())


class TrackableList(list):
    def append(self,object):
        print("Append called")
        super().append(object)


tl = TrackableList([])
tl.append(23)
print(tl)