# 'Match case' in python which is simlar to the 'switch case' in C

x = 5
#x is var to match
match x:
    case 0: # if x is zero
        print("x is zero")  
    
    case 4: #if x is 4
        print("x is 4")

    case _: #this default case , if nothing match then it will run as similar to else case
        print(x)    


Y = str(input("naam batao : "))

match Y:
    case 'pranshu':
        print("UDIT :- RAM RAM! bhai ji") 
    
    case 'vishal':
        print("UDIT :- batao muski kya haal")

    case _:
        print(Y +' tum list me nahi ho')    