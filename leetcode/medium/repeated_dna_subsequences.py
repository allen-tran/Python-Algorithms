def findRepeatedDnaSequences(s):
    # hashamp of string key and occurances value
    seenMap = {}
    res = []
    i= 0
    
    while i+10 <= len(s):
        tmp = s[i:i+10]
        if tmp not in seenMap:
            seenMap[tmp] = 1
        else:
            if tmp not in res:
                res.append(tmp)
        i+=1
    return res