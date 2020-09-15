n=int(input("enter a number until which u want to do prime number"))

for i in range(2,n):
        if (n%i==0):
                print("it is not a prime number")
                break
                
else:
        print("it is prime")

