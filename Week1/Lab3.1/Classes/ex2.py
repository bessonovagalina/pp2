class Shape:
    def area(self):
        print("This is not a square!")

class Square(Shape):
    def __init__(self,length):
        self.length=length
    
    def area(self):
        area=self.length**2
        print(f"Area of square:{area}")

length=float(input("Enter the length of a square:"))
square=Square(length)
#notsquare=Shape(0)
square.area()
#if length==0:
    #notsquare.area()