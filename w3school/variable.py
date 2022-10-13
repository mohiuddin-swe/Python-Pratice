print("#Many value to multiple variable")
x,y,z = "Orange","Banana","Cherry"

print(x)
print(y)
print(z)

print("................" )

print("#one value to multiple variable")
x=y=z = "Orange"

print(x)
print(y)
print(z)
print("................" )


print("# Unpack a Collection")

fruits = ["apple","banana","cherry"]
x,y,z= fruits
print(x)
print(y)
print(z)
print("................" )


x = "Python is awesome"
print(x)

x = "Python "
y = "is "
z = "Awesome"
print(x+y+z)

print("................" )

print("Printing Numbers")
x = 5
y = 10
print(x+y)
print("................" )

print("Printing Number and String Without + sign")
x = 5
y = "Mohiuddin"
print(x,y)
print("................" )


print("Global Variable")

x = "Awesome"

def myfunction():
    x = "Fantastic"
    print("Python is " + x)

myfunction()
print("python is "+ x)

print("................" )


print("Global Keyword Start from here")

def myfunc():
    global x
    x = "fantastic"

    myfunc()

    print("Python is " + x)
    print("x printed from a function through global keyword")
    print(".............................................")




