for number in range(3):
    print("Hello",number)
    
for number in range(3):
    print("Hello",number,(number+1)*".")
print(".........................")
    
for number in range(1,4):
    print("Hello again",number)
print(".........................")
for number in range(1,11,3):
    print("Hello again",number)
    
print(".........................")
attempt = False
for number in range(5):
    print("attempting for",number," times")
    if(attempt):
        print("attempt successfull")
        break
else:
    print("else block printed if the loop completed without breaking")
    
print("................................")

for x in range(3):
    for y in range(4):
        print(f"{x},{y}")
