try:
    x=int(input("enter the number1:"))
    y=int(input("enter the number2:"))
    z=x/y
except ZeroDivisionError:
    print("not divisible by zero")
except ValueError:
    print("invalid input")
