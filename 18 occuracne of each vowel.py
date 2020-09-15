a="abhinai"
v={"a","e","i","o","u"}
d={}
for i in a:
        if i in v:
                d[i]=d.get(i,0)+1
print(d)

for k,v in d.items():
        print("{} occurs {} times".format(k,v))
        
