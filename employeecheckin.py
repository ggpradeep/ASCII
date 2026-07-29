class Employee:
    def __init__(self):
        print("Employee made")
    def __del__(self):
        print("Employee destroyed")
def create_object():
        print("Creating object")
        obj = Employee()
        print("Function ends")
        return obj
print("Calling creating object() function")
obj = create_object()
print("Program end")