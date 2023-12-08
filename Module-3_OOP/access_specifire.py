class student:

    #private
    __id=12
    __name='Sanket'

    def __getdata(self):
        print("This is getdata.")

        print("ID:",self.__id)
        print("Name:",self.__name)

    def printdata(self):
        self.__getdata()

st=student()
#print(st.id)
#print(st.name)
#st.getdata()


st.printdata()