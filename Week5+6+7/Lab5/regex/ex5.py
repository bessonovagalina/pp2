import re

#word=str(input("Enter the string :"))

file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")

word= file.read()

pattern=r"^a+[a-z]+b$"

print(re.findall(pattern,word))