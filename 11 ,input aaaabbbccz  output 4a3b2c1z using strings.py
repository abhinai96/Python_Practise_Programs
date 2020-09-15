#aaaabbbccz
#4a3b2c1z
a="aaaabbbccz"
previous=a[0]
output=" "
c=0
i=0
while i<len(a):
        if a[i]==previous:
                c=c+1
        else:
                output=output+str(c)+previous
                previous=a[i]
                c=1
        if i==len(a)-1:
                output=output+str(c)+previous
        i=i+1
print(output)
                
                
