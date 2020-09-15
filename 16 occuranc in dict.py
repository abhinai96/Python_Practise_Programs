#abaabbca
#4a3b1c
a="abaabbca"
d={}
for i in a:
        d[i]=d.get(i,0)+1
print(d)
output=" "
for k,v in sorted(d.items()):
        output=output+str(v)+k
print(output)
        
