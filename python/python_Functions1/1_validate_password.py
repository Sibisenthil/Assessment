import re

pwd = input("Enter your password : ")
validpassword = True
Reason = ""

if len(pwd)<6 or len(pwd)>12:
    validpassword = False
    Reason = "Invalid length"
elif not re.search("[a-z]",pwd):
    validpassword = False
    Reason = "Lower case not found"
elif not re.search("[0-9]",pwd):
    validpassword = False
    Reason = "Invalid Numbers"
elif not re.search("[A-Z]",pwd):
    validpassword = False
    Reason = "Upper case not found"
elif not re.search("[$@#]",pwd):
    validpassword = False
    Reason = "Special character not found $@#"
if validpassword:
    print("ValidPassword")
else:
    print("Invalid Password. %s " %Reason)
