print("Create a Class")
print("...........................")

class MyClass:
    x = 5

print("Create Object")
print("...........................")
p1 = MyClass()
print(p1.x)


'''print("The_init_() Function")
print("...........................")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)'''

print("The__Str__() Function")
print("...........................")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



