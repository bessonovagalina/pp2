import os

def test_path(path):
    if os.path.exists(path):
        
        filename = os.path.basename(path)#получчаем имя файла
        print("Filename:", filename)
        
        directory = os.path.dirname(path)#получаем имя каталога
        print("Directory:", directory)
    else:
        print("Path does not exist.")

specified_path = input("Enter the specified path: ")
test_path(specified_path)
