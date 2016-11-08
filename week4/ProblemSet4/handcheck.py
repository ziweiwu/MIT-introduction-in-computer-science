from copy import deepcopy 
def isValidWord(word, hand, wordList):
    handcopy=(deepcopy(hand))
    for i in word:
        if i in handcopy and handcopy[i]>0 and word in wordList:
            print(i)
            handcopy[i]=handcopy[i]-1
            print(i, handcopy[i])
        else:
            return False
    return True
word='hammer'
hand={'a':1,'h':1,'m':2,'e':1,'r':1,'z':1}
wordList=['hammer','cat']
print(isValidWord(word,hand, wordList))
