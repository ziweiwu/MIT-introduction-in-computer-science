balance=3329

annualInterestRate=0.2

mi=annualInterestRate/12

mpmin=10

rb=balance

while rb>0:
    rb=balance
    mpmin=mpmin+10
    for i in range(12):
         rb=rb-mpmin
         rb=rb+rb*mi

print('Lowest Payment: ', int(mpmin)) 

    
    
        
