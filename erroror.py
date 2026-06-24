try:
    num1,num2 = eval(input("Enter 2 numbers, Seperated by a comma:"))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Divison by 0 is error")
except SyntaxError:
    print("Enter a comma between the 2 numbers")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will excucute no matter what")