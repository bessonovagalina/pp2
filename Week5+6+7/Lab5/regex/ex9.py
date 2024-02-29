import re

def insert_spaces(text):
    #                 (...) группа захвата, \1 обратная ссылка на группу захвата 
    result = re.sub(r"([A-Z][a-z]+)", r" \1", text)
    return result

file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")

text= file.read()
#text = str(input("Enter the string : "))
formatted_text = insert_spaces(text)
print(formatted_text)
