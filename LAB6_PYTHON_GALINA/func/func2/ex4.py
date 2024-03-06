from time import sleep
from math import sqrt

seconds = int(input())
numb = int(input())

sleep(seconds/1000)

print(f"Square root of {numb} after {seconds} miliseconds is {sqrt(numb)}" )
