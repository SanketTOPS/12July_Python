#global
a=34
b=56

def production():
    #local
    global a,b
    a=66
    b=89
    print("Mul:",a*b)

print("Sum:",a+b)

production()