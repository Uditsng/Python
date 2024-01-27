#fibonacci series
n = 10

a ,b ,c = 0, 1 ,0

print('fibonacci series : ') 

i = 1
while i <=n:
    c = a + b
    a = b
    b = c
    i = i + 1
    print(c, end=" ")
   