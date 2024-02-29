import re
res=''

file = open(r"Week5+6+7\Lab5\regex\row.txt", "r", encoding="utf8")

word= file.read()
#word=str(input("Enter the string:"))

pattern=re.compile(r"[a-z][A-Z]")
text=pattern.split(word)

for i in range(len(text)):
    res+=text[i].upper()
    print(" ".join(res))#выводит через пробелы

#добавила чтоб выводил через пробел 
