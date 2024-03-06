with open("1.txt", "r") as file:
    lines = file.readlines()
    num = len(lines) #len() считает количество строк
    print(num)