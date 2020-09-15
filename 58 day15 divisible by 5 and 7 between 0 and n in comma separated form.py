def fib(n):
        for i in range(1,n+1):
                if i%5==0 and i%7==0:
                        yield i
n=int(input("enter number"))
l=[]
for i in fib(n):
        l.append(str(i))
print(l)
c=",".join(l)
print(c)

                       
