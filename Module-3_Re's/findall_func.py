import re

mystr="This is String!"

#x=re.findall('This',mystr)
#x=re.findall('this',mystr)
#x=re.findall('is',mystr)
x=re.findall('S',mystr)
print(x)

if x: #bool
    print("Match done...")
else:
    print("Error!")