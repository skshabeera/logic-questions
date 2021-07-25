n=int(input("enter the number"))
a=n
rev=0
while n>0:
    b=n%10
    rev=rev*10+b
    n=n//10
if a==rev:
    print("pallindrome")
else:
    print("not pallindrome")