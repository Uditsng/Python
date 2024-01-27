#string methods in python

a = '        hey harry you are a gOOd teacher!'

print(a)
print(len(a))
print(a.lower()) #upper case
print(a.upper()) #lower case
print(a.replace('harry','harry bhai')) #replace specific word
print(a.rstrip()) #strip/cut extra space of right side
print(a.lstrip()) #strip/cut extra space of left side
print(a.split(' '))
print(a.capitalize()) #capitalise the 1st letter of word and lower case the other words
print(a.count('r'))
print(a.title()) 
print("\n")
print(a.center(50))

print(  "\n")

b = 'ram ram bhai'
print(b.endswith('bhai')) #search about ending word tell is true or false
print(b.endswith('ram',0,3))
print(a.endswith('harry',3,9))
print(a.find('are')) #it will find the index num
print(a.index('are')) #work same as .find

print("\n")

c = 'jay888'
print(c.isalnum()) #search for alpha numeric
print(c.isalpha()) # search for alphabets
print(c.islower()) #chech if all letter are lower case
print(c.isupper())
print(c.isnumeric())
print(c.isdigit())

print("\n")

d = "HEY i'm udit \n"   #\n is not printable
print(d.isprintable())
print(d.isspace())
print(d.startswith('hey'))
print(d.swapcase()) #upper to lower and lower to upper

