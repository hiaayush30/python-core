import sys

print(sys.argv) # first is always the name of the python program'

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <USERNAME>")
else:
    print("your username is ",sys.argv[1])