balance=320000

annualInterestRate=0.2

mi=annualInterestRate/12

pmin=balance/12

pmax=(balance+balance*annualInterestRate)/12

rb=balance

for j in range(100):
    rb=balance
    pmid=(pmin+pmax)/2
    for i in range(12):
        rb=rb-pmid
        rb=rb+rb*mi
    if rb>0:
        pmin=pmid
    elif rb<0:
        pmax=pmid
    else:
        pmid=pmid

print('Lowest Payment: ', round(pmid,2))







        
        



