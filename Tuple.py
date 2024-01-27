#tuples are immutable , i.e can't be modified
t1 = (1,6,9,4,1,9,75,82,46,"U","D","I","T")
print(type(t1))
print(t1,'\n')

#indexing of tuple
print("Indexing:",t1[8],"\n")
#slicing of tuple
print('Slicing:',t1[5:14:2],'\n')

#counting of a particular element occuring num of time
print('Counting 9:',t1.count(9),'\n')

print(t1.index(1))
