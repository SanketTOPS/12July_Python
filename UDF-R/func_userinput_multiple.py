def getdata():
    id=input("Enter ID:")
    nm=input("Enter Name:")
    ct=input("Enter City:")

    print("ID:",id)
    print("Name:",nm)
    print("City:",ct)


n=int(input("Enter number of students:"))
for i in range(n):
    getdata()

