products = input('Enter list of products')
prices = []
pricesSum = []
products_list = products.split(',')

for item in products_list: 
 prices.append(input('Enter list of prises').split(','))

for price in prices: 
 pricesSum.append(sum(list(map(int, price))))
 
result = max(pricesSum)
resultIndex = pricesSum.index(result)

print(prices)
print(f'{resultIndex}: {result}')