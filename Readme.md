- In python you can pass positional as well as named arguments
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Positional arguments (order matters)
greet("Alice", "Hi") # Output: Hi, Alice!

# Named arguments (order does NOT matter for the named ones)
greet(name="Bob", greeting="Greetings") # Output: Greetings, Bob!
greet(greeting="Good morning", name="Charlie") # Output: Good morning, Charlie!
```

- lambda fns (anonymous fns)
```python
# lambda parameters:expression
items.sort(key = lambda item:item[1])
```
---
```python
my_list = [3, 1, 4]

# Method: modifies the list in-place
my_list.sort()
print(my_list) # Output: [1, 3, 4]

# Built-in Function: returns a new sorted list, original list is unchanged
another_list = [5, 2, 8]
new_sorted_list = sorted(another_list)
print(another_list)     # Output: [5, 2, 8]
print(new_sorted_list)  # Output: [2, 5, 8]

# sort() is a method of list objects.
# sorted() is a built-in function (available globally like print() or len()).
```