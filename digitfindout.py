n=int(input("enter the number"))
a=n
while n>0:
    b=a%10
    n=n//10
if b==5:
    print("last number was 5")
else: 
    print("last number is not 5")
    
