def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    count=0

    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
                count=count+1
    print("Final L: ", L)
    print(count)



def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    count=0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
                count=count+1
                
    print("Final L: ", L)
    print(count)

L=[10,9,8,7,6,5,4,3,2,1]


modSwapSort(L)

