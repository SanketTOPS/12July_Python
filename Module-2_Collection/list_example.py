city=['rajkot','baroda','morbi','junagadh','jamnagar','surat']

"""print(city)
print(city[0])
print(city[-1])
print(city[0:4])
print(city[2:])
print(city[:4])

print(len(city))"""

# ------------------------------------- #
#print(city)

"""if 'morbi' in city:
    print("Yes...")
else:
    print("No..")"""

print(city.index('junagadh'))

#rajkot - 0
#baroda - 1

"""for i in city:
    print(i)"""

"""for i in city:
    print(f"{i} - {city.index(i)}")"""

"""n=0
for i in city:
    print(f"{i} - {n}")
    n+=1"""

# ------------------------------- #
print(city)
#city[4]='bhavnagar'
#city.append("gondal")
#city.insert(3,'wadhwan')
#city.pop()
#city.pop(2)
#city.remove('surat')
#city.clear()
#city.reverse()
#city.sort()
#del city
#print(city)


#newcity=city.copy()
#print(newcity)

newcity=['bhavnagar','navsari','diu','wadhwan']
print(newcity)

#print(newcity+city)
newcity.extend(city)
print(newcity)