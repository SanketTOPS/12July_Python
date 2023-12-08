"""def getsum(a,b):
    #print("Sum:",a+b)
    return a+b

def answer():
    x=getsum(23,45)
    print(x)

answer()"""


def getdata(id,name,sub):
    return id,name,sub


x=getdata(1,'Sanket','Python')
print(f"ID={x[0]}")
print(f"Name={x[1]}")
print(f"Sub={x[2]}")