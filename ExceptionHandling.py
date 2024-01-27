'''exception handling ka kaam hota hai jab user 
wrong input de de to program crash na ho aur na
hi error show kare instead hm ek chhota sa ms de 
paye invalid input ka''' 


try:  #suspicious piece of code
    n = int(input('Enter an integer: ')) 
    a = 7 / n
    print(a)
except:  #handling
    print("Invalid input")