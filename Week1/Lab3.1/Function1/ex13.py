import random

def guess():
    c = 1  
    name = input("Hello! What is your name? ")  # Не нужно оборачивать input в str(), input возвращает строку
    number = int(input(f"Well, {name}, I am thinking of a number between 1 and 20. Take a guess: "))
    
    target_number = random.randint(1, 20)  
    
    while number != target_number:  # Пока введенное число не равно загаданному
        if number < target_number:
            print("Your guess is too low. Take a guess.")
        else:
            print("Your guess is too high. Take a guess.")
        c += 1
        number = int(input()) 
    
    print(f"Good job, {name}! You guessed my number in {c} guesses!")

guess()
