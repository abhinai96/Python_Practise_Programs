n=int(input("enter a number"))
a=1
b=1
c=1
p=n
while a<=n:
        while b<=p:
                print(" ",end="")
                b=b+1
        while c<=a:
                print("*",end=" ")
                c=c+1
        print()
        p=p-1
        a=a+1
        b=1
        c=1
                
