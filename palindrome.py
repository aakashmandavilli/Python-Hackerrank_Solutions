def checkPalindrome(inputString):
    a=0
    b=len((inputString))-1
    while (a<b):   
        if inputString[a]==inputString[b]:
            a+=1
            b-=1
        else:
            return False
    return True
        
