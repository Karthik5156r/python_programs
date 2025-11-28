f=None
try:
    f=open("data.txt","r")
    data=f.read()
    print(data)
    #f.close()
except FileNotFoundError:
    print("something went wrong")
finally:
    if f is not None and not f.closed:
        f.close()
    
