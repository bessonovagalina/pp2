str1 = str(input("Enter the string: "))

def AZ(char):
    return ord('A') <= ord(char) <= ord('Z')

def az(char):
    return ord('a') <= ord(char) <= ord('z')

bigl = list(filter(AZ, str1))
smalll = list(filter(az, str1))

print(len(bigl), len(smalll))
