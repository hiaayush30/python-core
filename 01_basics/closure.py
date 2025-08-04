y = 10
def chaicoder(num):
    y = 1
    def actual(x):
        return (x*num)+y
    return actual

result = chaicoder(10)
print(result)
print(result(3))