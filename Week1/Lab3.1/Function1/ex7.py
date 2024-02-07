def three():
    list=input("Enter the list : ")
    numbs=list.split()
    numbs_list = [int(n) for n in numbs] 

    for i in range(len(numbs_list)-1):
        if numbs_list[i]==3 and numbs_list[i+1]==3:
            return True
        
    return False

result=three()
print(result)

