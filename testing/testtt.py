house_prices = {
    'Acorn Blvd': [0, 1, 2], 
    'Pine Ave': [4, 3, -9999],
    'Maple Lane': [3, -9999, 3, 3]
}
res = [[x for x in l if x >= 0] for l in house_prices.values()]
print(res)
print(house_prices.values())