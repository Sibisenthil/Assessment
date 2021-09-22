""""
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
    print("ValidPassword",pwd)
else:
    print("Invalid Password. %s " %Reason)
"""



#str = input("Enter the string : ")

#d=l=0

#for ch in str:
 #   if ch.isdigit():
#        d=d+1
  #  elif ch.isalpha():
   #     l=l+1
    #else:
     #   pass
#print("LETTERS ",l)
#print("DIGITS",d)

#dict={}
#def square(keys):
    #dict={}
   # for keys in range(1,21):
  #   print(dict)
#square(dict)






