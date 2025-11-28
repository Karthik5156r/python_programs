try:
    f=open("data.txt","r")
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("file not exist")
finally:
    print("file closed")

