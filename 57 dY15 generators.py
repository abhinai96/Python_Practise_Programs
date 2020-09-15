def fib(mymax):
        a,b=0,1
        while True:
                c=a+b
                if c<mymax:
                        yield c
                        a=b
                        b=c
                else:
                        break
fib(5)

                
