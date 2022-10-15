#Object Oriented Programming
#Inheritance

class A:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("Hello from class A")

class B(A):
    def __init__(self):
        pass
    def hello(self):
        print("Hello from class B")

obj = B()
obj.hello()
