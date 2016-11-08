lettersGuessed = ['e','i','k','p','r','s']

import string



def getAvailableLetters(lettersGuessed):
    allletters=list(string.ascii_lowercase)
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in allletters:
            allletters.remove(lettersGuessed[i])
    allletters=''.join(allletters)
    return allletters

print(getAvailableLetters(lettersGuessed))
  


