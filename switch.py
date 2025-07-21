try:
    day = int(input("Enter day between 0 and 6: "))
    match day:
        case 0:
            print("Monday")
        case 1:
            print("Tuesday")
        case 2:
            print("Wednesday")
        case 3:
            print("Thursday")
        case 4:
            print("Friday")
        case 5:
            print("Saturday")
        case 6:
            print("Sunday")
        case _:
            print("No such day")

    # or using it in a fn
    def weekend_or_weekday(day):
        match day: 
          case 0 | 1 | 2 | 3 | 4 :
                return "It's a weekday"
          case 5 | 6 :
              return "It's the weekend"
          case _:
            return "No such day"
    print(weekend_or_weekday(day))
except ValueError as ex:
    print("Enter a valid number")

month = int(input("Enter month between 0 and 11: "))
match month:
        case 0:
            print("January")
        case 1:
            print("February")
        case 2:
            print("March")
        case 3:
            print("April")
        case 4:
            print("May")
        case 5:
            print("June")
        case 6:
            print("July")
        case 7:
            print("August")
        case 8:
            print("September")
        case 9:
            print("October")
        case 10:
            print("November")
        case 11:
            print("December")
        case _:
            print("No such month")

def math_operations(a,b,operand):
    match operand:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case _:
            print("Not a valid operation")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
operand = input("Enter the operation i.e +,-,*,/:")
math_operations(a,b,operand)
