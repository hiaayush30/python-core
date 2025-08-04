# Pypi => Python Package Index

- we need features which are not implemented in the python standard library
- it's like npm
- it's a repo of python packages

---
- to install a package from pypi we use pip/pip3
```
   pip3 install requests==2.9.0
   pip3 install requests==2.9.*
```

- creating a virtual environment
```
cd <target-dir>
python3 -m venv venv 
source env/bin/activate
pip list > requirement.txt
deactivate
```

In the command `python3 -m venv venv`, the two instances of `venv` have completely different meanings and roles.

1.  **`python3 -m venv`**: Here, `venv` is a **module name**.
    * The `-m` flag tells the Python interpreter to "run the library module as a script."
    * So, `python3 -m venv` means "run the `venv` module that is included with Python 3."
    * The `venv` module is the built-in tool in Python 3 for creating and managing virtual environments. It's the core functionality.

2.  **`python3 -m venv venv`**: The second `venv` is an **argument** to the `venv` module. It's the name of the directory where the new virtual environment will be created.
    * This is a common convention, but you could name it anything you want.
    * For example, you could run `python3 -m venv my_project_env`. This would create a new directory named `my_project_env` inside your current directory, and all the files for the new virtual environment would be placed there.

### **Analogy**

Think of it like this:

`python3 -m venv <directory_name>`

* `python3`: The program you're running.
* `-m venv`: The command you're giving to the program, which is to use its built-in virtual environment creation tool.
* `<directory_name>`: The name you're giving to the new thing that the tool will create.

So, when you see `python3 -m venv venv`, you're essentially saying:

"Python 3, please run your virtual environment creator module, and name the new environment directory 'venv'."

- pipenv is a tool that combines pip and virtual environments into a single tool chain
- pipenv is equivalent to npm
- it internally uses pip and virtual environments