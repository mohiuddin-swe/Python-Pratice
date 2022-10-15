# Filter Function

l =[1,3,4,6,88,4,2,9,5]

def func(n):
    return n%2==1

newList = list(filter(func,l))

print(newList)

print("We also can use lamda function in filter function")

