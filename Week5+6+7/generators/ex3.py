def dis_gen(start, stop):
    while start <= stop:
        if start % 3 == 0 or start % 4 == 0:
            yield start #если return вообще не работает 
        start += 1

n = int(input("Enter the number: "))
dis_nums = list(dis_gen(1, n))
print(dis_nums)
