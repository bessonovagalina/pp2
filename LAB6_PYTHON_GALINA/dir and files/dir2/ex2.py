import os

def check_access(path):
    # Проверка существования пути
    if not os.path.exists(path):
        print("Path does not exist")
        return
    
    if os.access(path, os.R_OK):#читаемость
        print("Readable: Yes")
    else:
        print("Readable: No")
    
    if os.access(path, os.W_OK):#возможность записи
        print("Writable: Yes")
    else:
        print("Writable: No")
    
    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")

specified_path = input("Enter the specified path: ")
check_access(specified_path)
