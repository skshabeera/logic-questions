list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
list1.extend(list2)
new=[]
i=0
while i<len(list1):
    if list1[i]%2==1:
        new.append(list1[i])
    else:
        pass
    i=i+1
print(new)