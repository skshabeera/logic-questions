n=int(input("enter the number"))
if n%5==0 and n%11==0:
    print("both")
elif n%11==0:
    print("11")
elif n%5==0:
    print("5")
elif n%5!=0 or n%11!=0:
    print("none")
else:
    pass