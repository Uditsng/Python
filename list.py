#List is mutable ,can be modified
L = [ 8, 9, "udit", 5.009]
print(type(L))

#using indexing
print(L[2])

#using slicing
print(L[0:2])


print("\n")
# learning coping
s = [3,8, "udit", 8.909]
print(type(s))
print(s)

#coping element of S to P
P = s[:] #using[:] operator to copy
print(P)