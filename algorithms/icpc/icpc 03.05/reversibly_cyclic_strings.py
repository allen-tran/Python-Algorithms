
def is_cyc_sybstr(s, t):
    s = s + s[0:len(t)]
    return t in s

def main():
    string = input()

    for i in range(len(string)):
        for lenner in range(i+1,len(string)+1):
            if not is_cyc_sybstr(string, string[i:lenner][::-1]):
                print('0')
                return
    print('1')

# print(is_cyc_sybstr('fatcat', 'act'))
main()