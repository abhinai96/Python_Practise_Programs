#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
def lst():
        l=[]
        for i in range(1,21):
                c=i*i
                l.append(c)
                d=tuple(l)
        print(d)
        
lst()
        
        
