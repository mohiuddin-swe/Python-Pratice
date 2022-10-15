# Lamda function or annonymous function

# Normal Function
def add(x,y):
    return x+y

# Lamda function
add2 = lambda x,y: x + y

print(add2(10,15))


print("In one line ----IIFE")
print(".......................")

print((lambda x,y: x+y) (10,15))
