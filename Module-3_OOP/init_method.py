class studinfo:

    def __init__(self) -> None:
        print("This is init method!")

    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)


st=studinfo()
st.getdata(1,'Sanket')