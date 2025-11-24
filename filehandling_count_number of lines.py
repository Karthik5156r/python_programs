f=open("data.txt","r")
d=f.readlines()
count=0
for i in d:
    if i=="\n":
        continue
    count+=1
    print(i)
print(count)
f.close()
