fnm=input("Enter Firstname:")
lnm=input("Enter Lastname:")

#nested
if fnm.isupper() and lnm.isupper():

    email=input("Enter an email:")
    mobile=input("Enter a mobile number:")

    if email.islower() and mobile.isdigit():
        print("Firsname:",fnm)
        print("Lastname:",lnm)
        print("Email:",email)
        print("Mobile:",mobile)
    else:
        print("Error! Plz input valid email address or mobile")
else:
    print("Error!Plz input proper details!")