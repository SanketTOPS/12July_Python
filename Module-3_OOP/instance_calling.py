class student:
    id=1
    name="Sanket"

    def getdata(self):
        print("ID:",self.id)
        print("Name:",self.name)
    
#class calling using Object
"""st=student()
st.getdata()
st.id=23
st.name='Ashok'
st.getdata()"""


#class calling using Instance
student().getdata()
student().id=12
student().name="Nirav"
student().getdata()