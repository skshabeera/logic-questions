n=int(input("enter the number"))
a=n
while n>0:
    b=a//10
    c=b%10
    n=n//10
if c==3:
    print("3 is present")
else:
    print("3 is not present")
    
