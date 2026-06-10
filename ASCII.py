print("ASCII values")
string = input("Enter one character")
if type(string) is str and len(string) == 1:
    print("Valid")
else: 
    print("Please type one character")
if string >= 65 and string <= 90:
    print("This is uppercase")
elif string >= 97 and string <= 122:
    print("This is lowercase")
elif string >= 48 and string <= 57:
    print("This is from 0 to 9")
elif string == 32:
    print("This is space")
else:
    print("This is a special character")

    print(ord(string))