list=[1,2,3,4],[5,6,7,8],[9,10,11,12]
i=0
b=[]
while i<len(list[0]):
    a=[list[0][i],list[1][i],list[2][i]]
    b.append(a)
    i=i+1
print(b)

