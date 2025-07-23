class TagCloud:
    def __init__(self):
      self.__tags = {}  #this makes attribute privet (but still accessible, its focus is not on security more of a warning)

    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) + 1

    def __getitem__(self,key):
        return self.__tags.get(key.lower(),0)
    
    def __setitem__(self,key,count):
        self.__tags[key.lower()] = count

    def __len__(self):
        return len(self.__tags)
 
    def __iter__(self):
        return iter(self.__tags) 
    
cloud = TagCloud()

cloud.add("Python")
cloud.add("pythOn")
cloud.add("python")

print(cloud["python"])

cloud["java"] = 20
print(cloud["java"])

print(len(cloud))

for tag in cloud:
    print(tag)

# print(cloud.tags["PythOn"]) # this will throw error so we need to hide this attribute

print(cloud.__dict__)  # prints every attribute of the object
print(cloud._TagCloud__tags)