def unique_digits(input_list):
    unique_list = []
    
    for digit in input_list:
        if digit not in unique_list:
            unique_list.append(digit)

    return unique_list

list = input("Enter the list of digits separated by spaces: ")
digits = list.split()
digits2=(int(n) for n in digits)
result = unique_digits(digits2)
print(result)