class abhi:
        def __init__(self,name,age):
                self.n=name
                self.a=age
        def work(self):
                print(self.n)
                print(self.a)
                print("he works in wipro")
class yamu(abhi):
        def __init__(self,name,age,c,d):
                super().__init__(name,age)
                self.c=c
                self.d=d
        def kaam(self):
                print(self.c)
                print(self.d)
                print("she works in amazon")
o=yamu("abhi",20,"yamu",15)
o.work()
o.kaam()
                
                
