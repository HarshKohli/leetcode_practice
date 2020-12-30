# Author: Harsh Kohli
# Date created: 10/18/2020

def coinChange(coins, amount):
    if amount == 0:
        return 0
    dp = [0 for _ in range(amount + 1)]
    for coin in coins:
        if coin <= amount:
            dp[coin] = 1
            for index in range(amount + 1):
                if dp[index] != 0:
                    new_index = index + coin
                    if new_index <= amount:
                        new_num = dp[index] + 1
                        if dp[new_index] == 0 or new_num < dp[new_index]:
                            dp[new_index] = new_num
    if dp[amount] != 0:
        return dp[amount]
    return -1


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))
