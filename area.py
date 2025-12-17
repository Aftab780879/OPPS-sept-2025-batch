from abc import ABC,abstractmethod

class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        area= (21/7)*self.radius*self.radius
        print(f"Area of Circle = {area}")
        

class Rectangle(Shapes): 
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        area= self.l*self.b
        print(f"Area of rectangle= {area}")


circle=Circle(9)
circle.area()

rectangle=Rectangle(4,9)
rectangle.area()