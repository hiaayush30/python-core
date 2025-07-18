sentence = "This is a common interview question"
# for given text write a program to find out the most repeated letter in that given text 
from pprint import pprint

char_frequency={}

for letter in sentence:
        char_frequency[letter] = char_frequency.get(letter,0)+1

# maxValue = 0
# max_letter_repeated=""
# for x in char_frequency.items():
#         key,value=x
#         if(value>maxValue):
#              maxValue=value
#              max_letter_repeated=key
 
pprint(char_frequency,width=1) # width decides the number of characters on each line

#or

max_letter_repeated=sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True)
print(max_letter_repeated,"appeared the max number of times")
