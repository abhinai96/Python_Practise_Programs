#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
class circle:
        def __init__(self,radius):
                self.a=radius
        def new(self):
                area=(self.a**2)*3.14
                print(area)
o=circle(4)
o.new()
                
