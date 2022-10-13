#Dictionaries

#Key -> Value

#dict()

a = dict(key1 = 'Mohiuddin', key2 ='Dsc', key3='25')
b = {'key1': 'Mohiuddin', 'key2': 'Dsc', 'key3':'25'}
c = dict(zip(['key1','key2','key3'],['Mohiuddin','DSC','25']))

d= dict([('key1','Mohiuddin'),('key2','DSC'),('key3',25)])

e = dict({'key1': 'Mohiuddin', 'key2': 'Dsc', 'key3':'25'}) 

print(a)
print(b)
print(c)
print(d)
print(e)

print(e.pop('key1'))

x = list(c)
print(x)