from pathlib import Path
from zipfile import ZipFile

with ZipFile("9_python_standard_library/temp_files.zip","w") as zip:
   for path in Path("9_python_standard_library/ecommerce").rglob("*.*"): # find all files and direcotries and sub files in ecommerce
     print(f"writing {path} to zip file temp_files")
     zip.write(path)  # write them into this zip file
   zip.close()


with ZipFile("9_python_standard_library/temp_files.zip") as zip:
   print(zip.namelist()) # returns all the file names in the zip file
   info = zip.getinfo("9_python_standard_library/ecommerce/hi.txt")
   print(info.file_size)
  