#table of 2
for x in range(2,21,2): #range(start,stop,step/gap)
    print(  x ,end = ", ")
print('\n')

#list printing
l = [2,3,4,5,6,7,8,9] 
for i in l:
    print(i,end=" ")  

print('\n')
#multipling 2
for i in l:
    print(i*2,end=' ') 

print('\n')
#even loop
for i in l:
    if i % 2==0:
        print(i,end=' ')

print('\n')
l1 = ["udit hindu"]
for i in l1:
    print(i.upper())

print('\n')
l2 = []
for i in l:
    if i %2!=0:
        l2.append(i)
print(l2)