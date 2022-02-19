
def main():
    per = 'PER'
    a = input()
    new = per * (len(a) // 3)
    count = 0
    for i in range(len(new)):
        if new[i] != a[i]:
            count +=1
    print(count)
main()