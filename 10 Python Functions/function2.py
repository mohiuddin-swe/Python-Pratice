
def hello2(fname, lname= "Uddin"):


 print(f"Full Name: {fname} {lname}")

hello2("Md Mohi")


#Arbitary Keyword Arguments

def fun2(**kwargs):
    print(kwargs)

fun2(fname= "Md Mohi", lname= "Uddin", age=22)

fun2()