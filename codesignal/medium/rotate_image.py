def rotate(a):
    # create pointers for left, right, top, and bottom
    l, r = 0, len(a)-1
    
    while l < r:
        for i in range(r-l):
            t, b = l, r
            
            # save the top left value
            topLeft = a[t][l+i]
            
            # bottom left is assigned to top left
            a[t][l + i] = a[b-i][l]
            
            # bottom right is assigned to bottom left
            a[b-i][l] = a[b][r-i]
            
            # top right is assigned to bottom right
            a[b][r-i] = a[t+i][r]
            
            # topLeft saved variable gets assigne to top right
            a[t+i][r] = topLeft

        # shrink the square    
        l += 1
        r -= 1
        
    return a