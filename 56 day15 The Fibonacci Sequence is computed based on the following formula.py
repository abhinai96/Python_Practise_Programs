"""f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1"""
def fac(n):
        if n==0:
                return 0
        elif n==1:
                return 1
        else:
                return fac(n-1)+fac(n-2)
n=int(input("enter any number"))
print(fac(n))
