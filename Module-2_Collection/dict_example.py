stdata={'id':1,'name':'sanket','sub':'python'}

print(stdata)
#print(stdata['name'])
#print(stdata.get('name'))

#print(len(stdata))

print(stdata.keys())
print(stdata.values())

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

#stdata['id']=2
#stdata['city']='Rajkot'
#stdata.pop('sub')
#stdata.clear()
#del stdata['name']
#print(stdata)


newdict=stdata.copy()
print(newdict)