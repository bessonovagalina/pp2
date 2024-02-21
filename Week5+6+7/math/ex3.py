import math
n=float(input("Enter number of sides:"))
l=float(input("Enter the length of a side:"))
p=n*l #периметр
a=l/(2*math.tan(math.pi/n))#апофема
S=(a*p)/2
print(f"The area of the polygon is: {S}")
