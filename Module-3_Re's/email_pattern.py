import re


email="sanket_chauhan@gmail.com"

email_pattern="^[a-z0-9_]+[@]+[a-z]+[\.]+[a-z]"

x=re.findall(email_pattern,email)

if x: #true
    print("Email is valid")
else:
    print("Error! Invalid Email")
