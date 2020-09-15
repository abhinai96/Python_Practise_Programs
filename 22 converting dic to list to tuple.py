d={}
for i in range(1,6):
        d[i]=i*i
print(d)
#print(tuple(d))

lst=[]

for i in d:
        k=i,d[i]
        lst.append(k)
print(lst)

c=tuple(lst)
print(c)

