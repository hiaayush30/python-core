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
python3 -m venv env 
source env/bin/activate
deactivate
```

- pipenv is a tool that combines pip and virtual environments into a single tool chain
- pipenv is equivalent to npm
- it internally uses pip and virtual environments