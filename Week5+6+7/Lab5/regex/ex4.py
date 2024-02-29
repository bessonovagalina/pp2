import re
#word=str(input("Enter tha string :"))

file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")

word= file.read()

pattern=r"[A-Z]{1}+[a-z]+"

print(re.findall(pattern, word))