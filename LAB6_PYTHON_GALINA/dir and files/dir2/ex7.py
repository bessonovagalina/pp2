import os
source_file = "1.txt"#исходный файл

destination_file = "3.txt" #файл, в который будет скопировано все из 1.txt
command = f"cp {source_file} {destination_file}"#создаем команду, которая копирует все из первого во втторой

os.popen(command)#выполняет команду

