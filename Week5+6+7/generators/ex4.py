def square_gen(start, stop):
    while start <= stop:
        yield start ** 2 
        start += 1

a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
square_nums = list(square_gen(a, b))
print(square_nums)
