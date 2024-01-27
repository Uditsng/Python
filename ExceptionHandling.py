'''exception handling ka kaam hota hai jab user 
wrong input de de to program crash na ho aur na
hi error show kare instead hm ek chhota sa ms de 
paye invalid input ka''' 


try:  #suspicious piece of code
    n = int(input('Enter an integer: ')) 
    a = 7 / n
    print('a = ',a)
except Exception as p:  #handling , using Exception as we can see the miskate that is made
    print("Invalid input.", "heres the mistake that is made:", p)

finally: #this will be executed always
    b = 7 
    print('b = ',b)
