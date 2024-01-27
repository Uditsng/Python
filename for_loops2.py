list1 = [1,2,3,4,3,'u','d','i','t',8.009,True,False]
l_str = []
l_int = []
l_bool = []
for i in list1:
    if type(i) == str:
        l_str.append(i)
        print('string:',i,sep=' ')
    if type(i) == int:
        l_int.append(i)
        print('integer: ',i,sep=' ')
    if type(i) == bool:
        l_bool.append(i) 
        print('Bool:',i,sep=' ')       