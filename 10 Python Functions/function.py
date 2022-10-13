def hello (fname, lname):
    print(f"Full Name: {fname} {lname}")

hello("Md Mohi", "Uddin")

#Arbitrary Arguments

def fun1(*args):
    print(args)
    print(args[3])

fun1("Md","Mohi","Uddin",22,False)