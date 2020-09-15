#f(n)=f(n-1)+100 when n>0
#and f(0)=0

def fac(n):
        if n==0:
                
                return 0
        else:
                return fac(n-1)+100
n=int(input("enter any number"))
print(fac(n))

        
