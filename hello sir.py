list1=["hello","take"]
list2=["dear","sir"]
i=0
new=[]
while i<len(list1):
    j=0
    while j<len(list2):
        c=list1[i]+list2[j]
        new.append(c)
        j=j+1
    i=i+1
print(new)

