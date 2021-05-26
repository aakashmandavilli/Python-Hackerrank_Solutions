def adjacentElementsProduct(inputArray):
    a = -math.inf
    for i in range(0,len(inputArray)-1):
        b = inputArray[i]* inputArray[i+1]
        if b > a:
            a=b
    return a
