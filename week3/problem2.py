secretWord='apple'

lettersGuessed = ['e','i','k','p','r','s']

def getGuessedWord(secretWord, lettersGuessed):
    sw=list(secretWord)
#    print(sw)
    lg=lettersGuessed
#    print(lg)
    checkword=[]
    for i in range(len(sw)):
        if sw[i] in lg:
            checkword.append(sw[i])
        else:
            checkword.append(' _ ')
    checkword=''.join(checkword) 
    return checkword
             
print(getGuessedWord(secretWord, lettersGuessed))     
    

 

