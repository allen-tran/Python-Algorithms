def main():
    first_line = input()
    first_line = first_line.split(' ')
    num_obstacles = int(first_line[0])
    found = int(first_line[-1])
    setter = set()
    for i in range(found):
        setter.add(int(input()))
    # print(num_obstacles)
    count = 0
    for i in range(0, num_obstacles):
        if i not in setter:
            print(i)
        else:
            count+=1
            
    print(f'Mario got {count} of the dangerous obstacles.')

main()