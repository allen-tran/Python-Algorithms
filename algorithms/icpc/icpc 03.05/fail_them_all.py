def main():
    students, length_of_paper = input().split(' ')
    students = int(students)
    length_of_paper = int(length_of_paper)

    test = []
    banks = []
    count = 0
    for _ in range(students):
        answers = input()
        banks.append(answers)

    print(banks)

    for i in banks:
        for j in i:
            if j == 'X':
                test.append('F')
                continue
            if count < 1:
                if j == 'F':
                    test.append('F')
                    count += 1
                elif j == 'T':
                    test.append('T')
                    count += 1
            else:
                if j == 'F':
                    test.append('T')
                    count += 1
                elif j == 'T':
                    test.append('F')
                    count += 1
            
    print(test)
    # edited = []
    # for col in range(len(banks[0])):
    #     temp = []
    #     for row in range(len(banks)):
    #         temp.append(banks[row][col])
    #     edited.append(temp)

    # new = []

    # for i in edited:
    #     new.append(set(i))

    # for i in new:
    #     print(i)
    #     if count < 1:
    #         if 'T' in i and 'X' in i and 'F' in i:
    #             test.append('F')
    #             count += 1
    #         elif 'T' in i and 'X' in i:
    #             test.append('T')
    #             count +=1
    #         elif 'F' in i and 'X' in i and 'T' not in i:
    #             test.append('F')
    #             count += 1
    #     else:
    #         if 'T' in i and 'X' in i and 'F' in i:
    #             test.append('F')
    #             count += 1
    #         elif 'T' in i and 'X' in i:
    #             test.append('F')
    #         elif 'F' in i and 'X' in i and 'T' not in i:
    #             test.append('T')


    if count > 2:
        print(-1)
    else:
        print("".join(test))
main()