import re

def camel_to_snake(text):
    return re.sub(r'(?<=[a-z])([A-Z])', r'_\1', text).lower()

file_path = r"/Users/ruslanpashkevich/Desktop/LAB6_PYTHON_GALINA/dir and files/dir2/1.txt"
with open(file_path, "r", encoding="utf8") as file:
    camel_case = file.read()
    snake_case = camel_to_snake(camel_case)
    print(snake_case)
