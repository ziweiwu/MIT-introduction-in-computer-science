secretWord='apple'

lettersGuessed=['a','l','p','e','x','t']

#The idea is to check whether lettersguessed is the superset of secretword

def isWordGuessed(secretWord, lettersGuessed):
    sw=set(secretWord)
#    print(sw)
    lg=set(lettersGuessed)
#    print(lg)
    if lg>=sw:
        return True
    else:
        return False
            
           
            


print(isWordGuessed(secretWord, lettersGuessed))
