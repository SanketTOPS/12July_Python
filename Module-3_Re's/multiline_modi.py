import re

mystr="This is Python!"

#x=re.findall('^This',mystr)
#x=re.findall('^Python',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
#x=re.findall('on$',mystr)
x=re.findall('!$',mystr)
print(x)