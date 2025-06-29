letters = ['a','b','c','d','e']

print(letters[0])

letters[0] = "A"
print(letters)

letters.append("oyo")
print(letters)

print(letters[0:3])

letters_copy = letters
letters_copy[0] = "B"
print(letters)

letters_copy2 = letters[:]
letters_copy[0] = "YO"
print(letters)

print(letters[::2]) #returns every second element (starts from 1st)
print(letters[::-1])