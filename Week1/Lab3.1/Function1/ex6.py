def words():
    string = input("Enter a suggestion: ")
    words_list = string.split() #разделяем лист на элементы
    str_list = [str(word) for word in words_list]  # преобразуем в тип стр

    reverse_list = []
    for i in range(len(str_list) - 1, -1, -1):
        reverse_list.append(str_list[i])

    print(reverse_list)

words()