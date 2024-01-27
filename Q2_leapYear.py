#leap year
a = 2016
if a%400 == 0:
    print(a,': leap yr')
elif a%4==0 and a%100!=0:
    print(a,'leap yr')
else:
    print('NLY')    