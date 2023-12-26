coins = [500, 100, 50, 10]

exchange = int(input())

count = 0

for coin in coins:
    count += exchange // coin
    exchange %= coin

print(count)
