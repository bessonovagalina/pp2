def spy_game(nums):
    spy_sequence = [0, 0, 7]
    index = 0

    for num in nums:
        if num == spy_sequence[index]:
            index += 1
            if index == 3:
                return True
        elif num == spy_sequence[0]:
            # Если текущее число не совпадает с текущим элементом последовательности,
            # но равно первому элементу, начинаем проверку заново
            index = 1

    return False

# Пример использования:
user_input = input("Enter the list separated by spaces: ")
nums = [int(n) for n in user_input.split()]
print(spy_game(nums))