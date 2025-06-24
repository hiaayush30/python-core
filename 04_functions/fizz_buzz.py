def fizz_buzz(input):
    if input%3 == 0 and input % 5 ==0:
        print("fizz buzz")
    elif input%3==0:
        print("fizz")
    elif input%5==0:
        print("buzz")
    else:
        print(input)
        

fizz_buzz(15)
fizz_buzz(6)
fizz_buzz(10)
fizz_buzz(11)