stdata={}

keys=['id','name','sub']

for i in range(len(keys)):
    v=input(f"Enter a value of {keys[i]}:")

    stdata[keys[i]]=v

print(stdata)
