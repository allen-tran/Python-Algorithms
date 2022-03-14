def main():
    first = set(input())
    word = input()
    shortest = float('inf')
    n = int(input())
    res = []

    for i in range(n):
        line = input()
        s = []

        for i in range(len(line)):
            s.append(line[i])
        # point_u = 0
        # point_word = 0
        # while point_word < len(word) and point_u < len(line):
        #     if line[point_u] == word[point_word]:
        #         point_u += 1
        #     point_word += 1
        # print(s,'BEFORE')
        for i in range(len(word) - 1, -1, -1):

            if (len(s) == 0):
                continue
            if (word[i] == s[-1]):
                s.pop()
        # print(s, 'AFTER')
        if len(s) == 0:
            res.append(float('inf'))
        else:
            shortest = min(len(line), shortest)
            res.append(len(line))
        # if len(line) > len(word) and set(line) == set(word):
        #     res.append(float('inf'))
        # elif point_u == len(line):
        #     res.append(float('inf'))
        # else:
        #     shortest = min(len(line), shortest)
        #     res.append(len(line))
    # print(res)
    for i in res:
        if i == shortest and shortest != float('inf'):
            print(1)
        else:
            print(0)

    

main()