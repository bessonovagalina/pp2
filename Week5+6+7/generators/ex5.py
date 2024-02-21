def return_gen(start, stop):
    while start >= stop:
        yield start  
        start -= 1

n = int(input("Enter the number: "))
return_nums = list(return_gen(n, 1))
print(return_nums)
