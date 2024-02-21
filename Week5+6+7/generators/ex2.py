def even_gen(start, stop):
    while start <= stop:
        yield start 
        start += 2

n = int(input("Enter the number: "))
even_nums = list(even_gen(2, n))
print(even_nums)
