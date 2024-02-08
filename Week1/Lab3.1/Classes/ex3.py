class Shape():
   def __init__(self,length,width):
    self.length=length
    self.width=width

class Rectangle(Shape):
  def area(self):
    area=self.length*self.width
    print(f"Area: {area}")

length=float(input("Enter the lendth: "))
width=float(input("Enter the width: "))

rectangle=Rectangle(length,width)
rectangle.area()