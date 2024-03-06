import os

filename = "4.txt"

if os.access(filename, os.F_OK) and os.access(filename, os.X_OK):
    os.remove(filename)
else:
    print("file doesn't exist")