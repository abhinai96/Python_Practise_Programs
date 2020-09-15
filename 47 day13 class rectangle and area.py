#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class rectangle:
        def __init__(self,length,width):
                self.l=length
                self.w=width
        def area(self):
                area=self.l*self.w
                print("area of the rectangle is ",area)
o=rectangle(2,2)
o.area()
