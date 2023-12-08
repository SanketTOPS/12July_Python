

fl=open('newfile.txt','a')

"""fl.write(id)
fl.write(name)"""


n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a name:")

    fl.write(f"ID:{id}\nName:{name}\n")