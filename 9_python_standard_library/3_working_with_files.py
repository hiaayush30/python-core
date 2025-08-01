from pathlib import Path
from time import ctime
# shell utilities => for copying and moving directories and files
import shutil


path = Path("9_python_standard_library/ecommerce/hi.txt")
# path.exists()
# path.rename("innit.txt")
# path.unlink()
print(path.absolute())
print(path.stat())
print(ctime(path.stat().st_ctime))

with open("9_python_standard_library/ecommerce/hi.txt","r") as file:
    pass
# or
path.write_text("hello there")
print(path.read_text())

src = Path("9_python_standard_library/ecommerce/hi.txt")
target = Path("9_python_standard_library/ecommerce/hello.txt")
# target.write_text(src.read_text())
# or
shutil.copyfile(src,target)
