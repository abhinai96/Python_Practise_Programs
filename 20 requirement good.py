
#abhi,yamu,madhu
#aym,baa,hmd,iuh
x="abhi"
y="yamu"
z="madhu"
i=j=k=0
while i<len(x) or j<len(y) or k<len(z):
    output=" "
    if i<len(x):
            output=output+x[i]
            i=i+1
    if j<len(y):
            output=output+y[j]
            j=j+1
            
    if i<len(z):
            output=output+z[k]
            k=k+1
    print(output)





