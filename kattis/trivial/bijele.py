def bijele():
    need = [1, 1, 2, 2, 2, 8] # declares the values we need
    have = [int(x) for x in input().split()] # list comprehension. convert to integers. for x in the input (string) we will split them and store it in ist
    difference = [] # declare the difference list

    for i in range(len(need)): # for the need values
        difference.append(need[i] - have[i])

    print(" ".join([str(x) for x in difference]))

bijele()