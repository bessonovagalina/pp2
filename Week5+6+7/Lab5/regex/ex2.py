import re

file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")


word= file.read()
#word=str(input("Enter the string :"))
pattern=r"a{1}b{2,3}"
print(re.findall(pattern, word))