a=[12,10,15,67]
i=0
while i<len(a):
    sum=0
    while a[i]>0:
        n=a[i]%10
        sum=sum+n
        a[i]=a[i]//10
    i=i+1
    print(sum)
        
        
