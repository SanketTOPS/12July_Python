def getdata(data): #tuple argu
    print("ID:",data['id'])
    print("Name:",data['nm'])
    print("Subject:",data['sub'])

#getdata({'id':101,'nm':'Sanket','sub':'Python'}) #dict argument


stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")

getdata({'id':stid,'nm':stnm,'sub':stsub})