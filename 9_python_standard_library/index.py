from pathlib import Path


Path("/usr/local/bin") # absolute path
Path() # represents current folder
Path("ecommerce/__init__.py") # relative path ie in current folder go to ecommerce folder and so on


Path() / Path("ecommerce") # combining paths
#or
Path() / "ecommerce" / "__init__.py"

Path.home() # returns home directory of current use)


path = Path("ecommerce/__init.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)  # returns only the file name from the specified path