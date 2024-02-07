def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

prime= [number for number in list if is_prime(number)]

print("Prime numbers from the list:", prime)