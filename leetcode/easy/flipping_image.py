'''
#832 easy
'''

def flip(image):
        
    doublelist = []
    for i in image:
        newList = i[::-1]
        doublelist.append(newList)
        
    for i in (doublelist):
        for j in range(len(i)): 
            if i[j] == 1:
                i[j] = 0
            else:
                i[j] = 1
                    
    return doublelist

print(flip([[1,1,0],[1,0,1],[0,0,0]]))