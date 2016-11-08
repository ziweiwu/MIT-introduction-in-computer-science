 def checkhand(word, hand):
        from copy import copy 
        handcopy=(copy(hand))
        for i in word:
            if i in hand and hand[i]>0:
                hand[i]=hand[i]-1
            else:
                return False
            return True
        
