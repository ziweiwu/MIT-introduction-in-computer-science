import string

secretWord='apple'

def isWordGuessed(secretWord, lettersGuessed):
    sw=set(secretWord)
#    print(sw)
    lg=set(lettersGuessed)
#    print(lg)
    if lg>=sw:
        return True
    else:
        return False

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
 
def getAvailableLetters(lettersGuessed):
    allletters=list(string.ascii_lowercase)
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in allletters:
            allletters.remove(lettersGuessed[i])
    allletters=''.join(allletters)
    return allletters


def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long' %len(secretWord))
    print('-----------')
    lettersGuessed=[]
    count=8 
    while count>0:
        print('You have ',count ,' guesses left')
        print('Available Letters: %s' %getAvailableLetters(lettersGuessed))
        letterinput=(input('Please guess a letter: '))

        if letterinput in secretWord:
            if letterinput in lettersGuessed:
                print("Oops! You've already guessed that letter: %s"  %getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(letterinput)       
                print('Good guess: %s' %getGuessedWord(secretWord, lettersGuessed)) 

        else:
            if letterinput in lettersGuessed:
                print("Oops! You've already guessed that letter: %s"  %getGuessedWord(secretWord, lettersGuessed))
            else:
                count=count-1
                lettersGuessed.append(letterinput)     
                print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))


        print('-----------')    

        if isWordGuessed(secretWord, lettersGuessed):
            break
        else:
            continue

    if isWordGuessed(secretWord, lettersGuessed):
        print ('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was %s.' %secretWord)

    
                



hangman(secretWord)
