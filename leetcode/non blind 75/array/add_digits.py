'''
https://leetcode.com/problems/add-digits/
'''

def addDigits(self, num: int) -> int:
    
    # summer = 0
    while len(str(num)) > 1:
        summer = 0
        for dig in str(num):
            summer += int(dig)
        num = summer
        print(num)
        
    return num
    