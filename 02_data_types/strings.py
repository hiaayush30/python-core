

str = "Hello World"
print(str[0])
print(str.split(" ")[0])
#or
print(str[0:5])

numList = "0123456789"
# print(numList[:7])
# print(numList[:])
# print(numList[5:])
# print(numList[0:7:2])  #2 next 2nd number
# print(numList[::3])

print(str.lower())
print("     yo    ".strip())
print(str.replace("Hello","Yo"))
print(str.find("hey"))
print("hey hey hey".count("hey"))

str2 = ":)"

sentence = "{},yo there {}"
print(sentence.format(str,str2))


li = ["hello","there"]
print(":".join(li))
print(len(str))

for letter in str:
    print(letter)

str3 = "He said:\"the movie was amazing\""
print(str3)

str4 = r"hello there \"\n yo"  # everything after r is treated as raw string
print(str4)

str5=r"c:\users\home"
print(str5)

print("hello" in str)