balance=42

annualInterestRate=0.20

monthlyPaymentRate=0.04


monthlyir = annualInterestRate/12

rb=balance


for i in range(12):
    mp = monthlyPaymentRate * rb
    rb=rb-mp
    rb=rb+rb*monthlyir

print('remaining balance: ',round(rb,2))
    
    





