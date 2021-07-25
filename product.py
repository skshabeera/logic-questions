n=int(input("enter the number"))
i=0
product=1
while n>0:
    product=product*(n%10)
    n=n//10
    i=i+1
print(product)