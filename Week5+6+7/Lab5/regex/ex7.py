import re

def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")

snake_case= file.read()
#snake_case = str(input("Enter the string :"))
camel_case = snake_to_camel(snake_case)
print(camel_case)


