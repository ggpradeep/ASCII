#ValueError, ZeroDivisionError, TypeError, SyntaxError
try:
 num = int(input("What is your age"))
except TypeError:
    print("Please type your age")
except SyntaxError:
    print("Make sure you typed the right thing")
except ValueError:
    print("Type a number")
else:
   if num % 2 == 0:
      print("Your age is even")
   else:
    print("Your age is odd")