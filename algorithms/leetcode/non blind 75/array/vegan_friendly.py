def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    ans = []
    
    for r in restaurants:
        if r[3] <= maxPrice and r[4] <= maxDistance:
            if veganFriendly == 1 and r[2] != 1:
                continue
            ans.append(r)
    ans = [x[0] for x in sorted(ans, key=lambda x: (-x[1], -x[0]))]
    
    return ans