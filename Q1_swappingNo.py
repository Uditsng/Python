#swapping two number without taking a temp var.
 
a = 10
b = 4
print('Before swapping:a = ',a,' and b = ' ,b)

a = a + b
b = a - b
a = a - b
print('after swapping: a = ',a,' and b = ',b)