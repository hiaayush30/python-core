year = 2025  

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,":its a leap year")
else:
    print(year,":not a leap year") 


income = True
good_credit = True
student = True

if good_credit and income:
    print("awsome")

if not income:
    print("why no income?")

if (income or good_credit) and not student:
    print("yo")

# short circuit evaluation
# the conditionals in python are short cicuited,example in case of and operator
# if the first one is false then the whole expression is false regardles what comes operator comes after that

if income or good_credit and not student:
    print("ho")
