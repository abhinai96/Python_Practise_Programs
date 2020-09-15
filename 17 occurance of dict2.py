#abaabbca
#a4b3c1
a="abaabbca"
d={}
for i in a:
        d[i]=d.get(i,0)+1
print(d)
output=" "
for k,v in sorted(d.items()):
        output=output+k+str(v)
print(output)
        
