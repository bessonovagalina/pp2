def palindrome():
    string=str(input("Enter the string : "))
    reserve=string[::-1]
    return string==reserve

result=palindrome()
print(result)

#string=str(input("Enter the string : "))
if result is True: print ("is a palindrome")
else : print ("isn't a palindrome")