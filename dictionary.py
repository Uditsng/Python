dict1 = {1 : 'a',2:'b',3:'c',4:'d',9:'p',6:'r',6:'e'}
dict2 = {'a':'pass','b':'pass+','c':'pass++'}
# print(dict1[3])
# print(all(dict1))
# print(len(dict1))
# print(sorted(dict1))

# print(dict1.copy())

print(dict1.keys())
print(dict1.items())
print(dict1.values())

#update : dict1 = dict1 + dict2
dict1.update(dict2)
print(dict1)
