from timeit import timeit

code1="""
def calculate_xfactor(age):
    if age<=0:
        raise ValueError("Age cannot be zero or less")
    return 10/age

try:
    calculate_xfactor(0)
except ValueError as ex:
    # print(ex)
    pass  # do nothing
"""

code2="""
def calculate_xfactor(age):
    if age<=0:
        return None
    return 10/age

    x_factor  =  calculate_xfactor(0)
    if x_factor == None:
       pass
"""

execution_time=timeit(code1,number=10000)
execution_time2=timeit(code2,number=10000)
print(execution_time)
print(execution_time2)