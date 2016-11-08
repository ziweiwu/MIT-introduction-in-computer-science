trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
                  '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    ''' 
    string=''
    if len(us_num)==1:
        string=trans[us_num]
    else:        
        for i in us_num:
            if i in trans and trans[i]!='ling': 
                string=string+trans[i]+' '+'shi '
            else:
                string=string+trans[i]
        string=string[:-5]
        if string[0:2]=='yi':
            string=string[3:]

    return string



print(convert_to_mandarin('16'))
       
print(convert_to_mandarin('22'))

print(convert_to_mandarin('2'))
