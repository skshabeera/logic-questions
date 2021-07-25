list1=[1,2,3]
list2=[3,1,4]
i=0
a=[]
while i<(len(list1)):
    j=0
    while j<(len(list2)):
        if list1[i]!=list2[j]:
            a.append(list1[i])
        j=j+1
    i=i+1
print(a)
# a=[]
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x!=y:
#             a.append((x,y))
# print(a)

