numbers = [1,2,3]
print(*numbers)  # it is the same as spread operator in js

# unpacking operator can be used to spread any iterable
list = [*range(10),*"Hello"]
print(list)

another_list = ["yo","bro"]

combined_list = [*list,*another_list]
print(combined_list)

first_dict = {"x":5}
second_dict = {"y":"2","x":"3"}
combined = {**first_dict,**second_dict,"z":3}  #multiple same keys, then last one will be taken
print(combined)