"""a=["abhi","yamu"]
b=[20,30]
print(dict(zip(a,b)))"""

a="a4b5"
l=[]
k=[]
for i in a:
        if i.isalpha():
                l.append(i)
        else:
                k.append(i)
print(l)
print(k)
print(dict(zip(l,k)))
