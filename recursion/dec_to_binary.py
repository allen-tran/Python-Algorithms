'''
Convert a number from decimal to binary using recursion
Step 1:
    divide the number by 2
Step 2:
    get the integer quotient for the next iteration
Step 3:
    get the remained for the binary digit
Step 3++:
    repeat the steps until the quotient is equal to 0
'''

def convert(dec):
    assert int(dec) == dec, "Decimal number must be an integer"
    if dec == 0:
        return dec
    else:
        return (dec % 2) + 10 * convert(dec // 2)

print(convert(10))
