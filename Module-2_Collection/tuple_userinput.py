data=[]

n=int(input("Enter number of elements:")) #n=5

for i in range(n):
    x=input("Enter an elements:")
    data.append(x)

print(tuple(data))
