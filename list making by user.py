
i=0
b=[]
while i<10:
    num=int(input("enter the number"))
    b.append(num)
    if num%2==0:
        print(num*100)
    else:
        print(num*-1)
    i=i+1
print(b)