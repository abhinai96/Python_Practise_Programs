#B4A1D3
#ABD134
a="B4A1D3"
#b=a.split()
#print(b)
c=sorted(a)
print(c)
alphabets=[]
digits=[]
for i in c:
        if i.isalpha():
                alphabets.append(i)
        else:
                digits.append(i)
d=alphabets+digits
e=" ".join(d)
print(e)
        
