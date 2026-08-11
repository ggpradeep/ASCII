class myClass:
    __privateVar = 12
    def __privMeth(self):
        print("I'm inside class: myClass")
    def hello(self):
        print("Private variable = ",myClass.__privateVar)
foo = myClass()
foo.hello()
foo._myClass__privMeth()