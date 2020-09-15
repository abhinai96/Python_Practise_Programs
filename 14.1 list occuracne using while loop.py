a=[1,2,2,3,3,3,3,4,4,5,5]
output=[]
i=0
while i<len(a):
        if a[i] not in output:
                output.append(a[i])
        i=i+1
print(output)
                

