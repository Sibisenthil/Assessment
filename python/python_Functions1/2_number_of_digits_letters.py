str = input("Enter the string : ")

d=l=0

for ch in str:
    if ch.isdigit():
        d=d+1
    elif ch.isalpha():
        l=l+1
    else:
        pass
print("LETTERS ",l)
print("DIGITS",d)
