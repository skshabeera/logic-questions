vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
n=input("enter the string")
a=0
b=0
i=0
while i<len(n):
    if n[i] in vowels:
        a=a+1
    if n[i] in consonents:
        b=b+1
    else:
        pass
    i=i+1
print(a, "vowels count")
print(b,"consonents count")


