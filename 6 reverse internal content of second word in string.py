#abhinai yamuna madhu aditya
#abhinai anumay madhu aytida
a="abhinai yamuna madhu aditya"
b=a.split()
print(b)
l=[]
i=0
while i<len(b):
        if i%2==0:
                l.append(b[i])
        else:
                l.append(b[i][::-1])
        i=i+1
print(l)
