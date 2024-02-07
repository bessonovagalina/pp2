import math

def volume():
    R=float(input("Enter the radius: "))
    V=(4*math.pi*R**3)/3
    print(f"Volume : {V}")

volume()