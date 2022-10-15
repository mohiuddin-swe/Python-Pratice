#Map Function

def func(n):
    return n*n*n

l = [3,4,1,0,6]

newL = list(map(func, l))
print(newL)

newL = tuple(map(func, l))
print(newL)

newL = set(map(func, l))
print(newL)

print("Lambda function in Map function")
print(".............................")

newL= list(map(lambda n: n*n*n,l))
print(newL)

l = ['Md Mohiuddin','Daffodil Swe','Dsc']

l2 = list(map(list,l))
print(l2)