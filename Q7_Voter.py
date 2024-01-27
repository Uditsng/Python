#program to select right people thst can vote

nationality = input('Nationality : ')
age = int(input('How Old You Are : '))
Voter_ID = input("Have Voter ID (yes/no) :")

if nationality == 'BHARAT'or 'Bharat' or 'bharat':
    if age > 17:
        if Voter_ID == 'YES' or 'yes' or 'Yes':
            print('you can vote')
        else:
            print('you cannot vote')    
    else:
        print('under-age')    
else:
    print('Not Citizen of BHARAT')    