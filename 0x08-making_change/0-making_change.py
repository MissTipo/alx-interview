#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    memo = {}  # Memoization dictionary

    def dp(amount):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        minCoins = float('inf')  # Initialize with infinity

        for coin in coins:
            subproblem = dp(amount - coin)
            if subproblem >= 0:
                minCoins = min(minCoins, subproblem + 1)

        memo[amount] = minCoins if minCoins != float('inf') else -1
        return memo[amount]

    return dp(total)
