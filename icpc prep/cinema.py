def main():
    first = input().split(' ')
    a, b = int(first[0]), int(first[1])
    count = 0
    second = input().split(' ')
    for i in range(len(second)):
        if int(second[i]) <= a:
            a -= int(second[i])
        else:
            count += 1

    print(count)
main()
