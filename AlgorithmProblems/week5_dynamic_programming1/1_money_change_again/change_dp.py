def change(money):
    # write your code here
    coins = [1, 3, 4]

    dp = [money + 1] * (money + 1)
    dp[0] = 0

    for amount in range(1, money + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[money] if dp[money] != money + 1 else -1

if __name__ == '__main__':
    m = int(input())
    print(change(m))
