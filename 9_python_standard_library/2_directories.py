from pathlib import Path
path = Path(r"9_python_standard_library/ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")


print(path.iterdir()) # returns a generator object which is a list of files and dirs in this path

print(path.absolute())

for p in path.iterdir():
    print(p)

# or using list comprehension express
paths = [p for p in path.iterdir() if p.is_dir()]  # only directories
print(paths) # an array of posix path objects (in mac/linux)
# the imported pathlib class is a base class for posix path objects and windows path objects
# but it has limitations:
# can't search by pattern
# does't search recursively
print("*****************")

path.glob("*.py") # returns a generator object
text_files = [p for p in path.glob("*.txt")]
print(text_files)
# to search recursively
# use "**/*.py"
# or
text_files = [p for p in path.rglob("*.txt")]