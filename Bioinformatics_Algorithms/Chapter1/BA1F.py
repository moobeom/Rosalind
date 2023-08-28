### Find a position in a genome minimizing the skew ###

def SkewMin(text):
    skew = 0
    valueDict = {'A':0, 'C':-1, 'G':1, 'T':0}
    skewList = []
    for i in range(len(text)):
        skew += valueDict[text[i]]
        skewList.append(skew)

    skew_min = min(skewList)
    indexList = []
    for i in range(len(skewList)):
        if skewList[i] == skew_min:
            indexList.append(i)
    return indexList