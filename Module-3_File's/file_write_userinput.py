id=input("Enter an ID:")
name=input("Enter a name:")

fl=open('newfile.txt','w')

fl.write(id)
fl.write(name)