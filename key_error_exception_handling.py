my_dict={'a':'b','c':'d'}
try:
    print(my_dict['d'])
except KeyError:
    print("invalid key")
    
