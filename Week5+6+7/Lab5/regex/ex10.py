import re

def camel_to_snake(text):                 #все с маленькой буквы, lstrip удаляет то, что в ()
    return re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')

#camel_case = str(input("Enter the string: "))
file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")

camel_case = file.read()
snake_case = camel_to_snake(camel_case)
print(snake_case)
#если слово полностью из заглавных букв, разделяет тоже (