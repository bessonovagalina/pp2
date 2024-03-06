import os
import re

path_to_folder = './dir/'

pattern = re.compile('[A-Z]')

for i in pattern.findall('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    with open(os.path.join(path_to_folder, f"{i}.txt"), "w") as file: #os.path.join() используется для объединения пути к каталогу и имени файла
        file.write(f"This is {i}.txt, it was created and written from 6.py")
