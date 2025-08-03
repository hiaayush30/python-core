import subprocess


# result = subprocess.run(["ls","-l"])
# result = subprocess.run(["ls","-l"],capture_output=True,text=True) # now result will not be printed but captured
# result = subprocess.run(["python3","./9_python_standard_library/other.py"],capture_output=True,text=True) 
try:
    result = subprocess.run(["false"],
                        capture_output=True,
                        text=True,
                        check=True) # will automatically raise exception  
    print(type(result))

    print("returncode:",result.returncode) # non zero value indicates an  error
    print("args:",result.args)
    print("stderr:",result.stderr)
    print("stdout:",result.stdout) 

# if result.returncode != 0 :
#     print(result.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)