stdata={}


keys=['id','name','sub']

n=int(input("Enter number of pairs:"))

for i in range(n):
    k=input("Enter Key:")
    v=input("Enter Value:")

    stdata[k]=v

print(stdata)