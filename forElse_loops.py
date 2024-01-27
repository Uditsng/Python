n = [1,2,3,4,5,6,7,7,8,9,]
for i in n:
    print(i,end=' ' )
else:
    print('this line will only executed when loop has no value remain unvisited')

print("\n")

n = [1,2,3,4,5,6,7,7,8,9,]
for i in n:
    print(i,end=" ")
    if i == 5:
        break
else:
    print('this line will only executed when loop has no value remain unvisited')

print('\n \n \n')