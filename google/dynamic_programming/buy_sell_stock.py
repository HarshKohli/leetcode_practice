# Author: Harsh Kohli
# Date created: 10/18/2020

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    lowest = prices[0]
    max_profit = 0
    for index in range(1, len(prices)):
        price = prices[index]
        if price < lowest:
            lowest = price
        else:
            profit = price - lowest
            if profit > max_profit:
                max_profit = profit
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
