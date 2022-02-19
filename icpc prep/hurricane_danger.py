def sqrdist(x, y, m, b):
    try:
        c = y + x
        closestx = (c - b) / (m + 1)
        closesty = m * closestx + b
    except ZeroDivisionError:
        return float('inf')
    except:
        return None
    #print(f'{c=}, {m=}, {b=}')
    #print(f'closest point at {closestx} {closesty}')
    return (closestx - x)**2 + (closesty - y)**2

n = int(input())
for i in range(n):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
    yintercept = y2 - slope * x2 if slope != float('inf') else float('-inf')
    print(f'y = {slope} x + {yintercept}')
    minlist = []
    minval = float('inf')
    m = int(input())
    for j in range(m):
        name, x, y = input().split()
        x = int(x)
        y = int(y)

        dist = sqrdist(x, y, slope, yintercept)
        #print(f'{name} has {dist=}')
        if dist < minval:
            minlist = [name]
            minval = dist
        elif abs(dist - minval) == 0:
            minlist.append(name)
    print(' '.join(minlist))
