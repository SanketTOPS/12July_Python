class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("This is student class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


# Object of class
st=student()
print("ID:",st.stid)
print("Name:",st.stnm)

st.getdata()
st.getsum(12,34)