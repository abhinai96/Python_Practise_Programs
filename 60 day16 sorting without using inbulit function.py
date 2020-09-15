a=[20,10,15,12,31]
for i in range(len(a)):
        min_val=min(a[i:])
        min_ind=a.index(min_val)
        a[i],a[min_ind]=a[min_ind],a[i]
print(a)
        
