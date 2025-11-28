try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    c=a/b
except ZeroDivisionError:
    print("cant divisible by zero")
else:
    print(c)
    
    
