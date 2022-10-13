#tuple, range, dictionary,list

myTuple =("a","b","c","d")
for x in myTuple:
    print(x)

myList= {("a", 1, "BDT"),("b", 2, "RUPEE"),("c", 3, "DOLLAR")}
for m,n,o in myList:
    print(f"{m},{n},{o}")


#dictionary Looping

myDict = {"Name": "Mohiuddin", "age": 22, "country": "Bangladesh"}

for key, value in myDict.items():
    print(f"{key} => {value}")


# characqter looping

myStr = "Software"

for ch in myStr:
    print(ch)


mySet = {"BDT","USD","CAD"}

for currency in mySet:
    print(currency)


