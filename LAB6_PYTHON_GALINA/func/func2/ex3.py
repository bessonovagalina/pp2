def palindrome():
        str1=str(input("Enter the string : "))
        reversed_word = ''.join(reversed(str1))
        if reversed_word==str1:
            print("yes, this is a palindrome ;)")
        else:
            print("no ;(")  
              
palindrome()

