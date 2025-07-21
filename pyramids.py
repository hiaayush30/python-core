rows = int(input("Enter number of rows:"))
if(rows<=0):
    print("Enter valid number of rows")
    exit()

count=1
while(count<=rows):
    for number in range(count):
        print("*",end="")
    print("")        
    count+=1

# or
print("\n")

for i in range(1,rows+1):  # range(start,stop) stop is not included
    print(" " * (rows-i),end="")
    print("*"*i)

print("\n")

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

print("\n")

for i in range(1,rows+1):
    for j in range(1,rows-i+2):
        print(j,end=" ")
    print("")

print("\n")

for i in range(1,rows+1):
    for j in range(1,rows-i+2):
        print(rows+1-j-i+1,end=" ")
    print("")