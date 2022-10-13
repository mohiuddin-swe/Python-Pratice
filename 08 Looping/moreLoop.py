myList = ['apple','orane','apple','pear','orange','banana']
myList2 =[1,2,3,4,5,6]

#enmerate
#for fruit in enumerate(myList):
    #print(fruit)

#zip 
for i,j in zip (myList2, myList):
    print(i,j)

for i in sorted(myList):
    print(i)

for j in reversed(sorted(myList)):
    print(j)
