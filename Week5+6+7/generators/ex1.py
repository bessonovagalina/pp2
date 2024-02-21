def square_gen(start, stop):
    while start <= stop:
        yield start ** 2 
        start += 1

n = int(input("Enter the number: "))
square_nums = list(square_gen(1, n))
print(square_nums)
