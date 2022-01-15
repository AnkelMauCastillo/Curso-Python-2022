#dict
dic = dict(nombre = 'Angel', apellido = 'Castillo', edad = 22 )
print (dic)

#zip
dic = dict(zip('abcd',[1,2,3,4]))
print (dic)

#items
print (dic.items())

#keys
print (dic.keys())

# copy 
dic1 = dic.copy()


# clear

print (dic1.clear())

# fromkeys

dic1 = dict.fromkeys(['a', 'b', 'c', 'd'], 1)
print (dic1)

# get
print (dic.get('b'))

# pop

print (dic.pop('b'))

print (dic)

# setdefault

print (dic.setdefault('a'))
print (dic)


# setdefault forma 2

print (dic.setdefault('e', 5))
print (dic)

# update
d1 = {'a':10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print (d1)


