grade_types={"A":"great","B":"Good","C":"OK","D":"Poor"}

print(grade_types)

print(grade_types.get("A")) #this will return nothing if not found

print(grade_types["B"])  #this will return error if not found


grade_types["C"]="Bad"
for i in grade_types:
    print(i+":"+grade_types[i],end="\n")

#for dictionary objects you can also do -
print(grade_types.items())
for key, value in grade_types.items():
    print("key is ",key+" and value is ",value,end="\n")

if "A" in grade_types:
    print("THis dictionary has the A key")

print(len(grade_types))

grade_types["E"] = "Bhai?!"
# grade_types.pop("E") #requires key as argument
# grade_types.popitem()
del grade_types["A"]  # removes reference from the memory itself
print(grade_types)

grade_types2= grade_types.copy()

tea_shop = {
   "teaShop1": {
       "Masala":10,
       "Ginger":20
    },
    "teaShop2":{
        "Masala":15,
        "Ginger":30
    }
}
print(tea_shop["teaShop1"]["Masala"])

squared_nums = { x:x**2 for x in range(6)}
# squared_nums.clear()
print(squared_nums)

keys=["Masala","Ginger","Green"]
default_val="Delicious"

new_dict = dict.fromkeys(keys,default_val)
print(new_dict)