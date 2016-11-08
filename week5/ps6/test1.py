def shift_dict(shift):
    import string
    letter_lower=list(string.ascii_lowercase)
    letter_lower_shift=[]
    for i in letter_lower:
        if ord(i)+shift>122:
            letter_lower_shift.append(chr((ord(i)+shift-122+96)))
        else:
            letter_lower_shift.append(chr(ord(i)+shift))
    
    
    letter_upper=list(string.ascii_uppercase)
    letter_upper_shift=[]
    for i in letter_upper:
        if ord(i)+shift>90:
            letter_upper_shift.append(chr((ord(i)+shift-90+64)))
        else:
            letter_upper_shift.append(chr(ord(i)+shift))
    

    letter=letter_upper+letter_lower
    letter_shift=letter_upper_shift + letter_lower_shift
    dict_shift=(dict(zip(letter, letter_shift)))

    return dict_shift 

print(shift_dict(4))

print(shift_dict(1))

