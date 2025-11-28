lst=[1,2,3,4]
try:
    print(lst[7])
except IndexError:
    print("item not found")
