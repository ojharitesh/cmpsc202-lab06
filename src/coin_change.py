def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")

    best = float("inf")
    for coin in coins:
        best = min(best, coin_change_recursive(coins, amount - coin))

    return best + 1 if best != float("inf") else -1


def coin_change_memoized(coins, amount, memo=None):
    if memo is None:
        memo = {}

    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")
    if amount in memo:
        return memo[amount]

    best = float("inf")
    for coin in coins:
        best = min(best, coin_change_memoized(coins, amount - coin, memo))

    memo[amount] = best + 1 if best != float("inf") else -1
    return memo[amount]


def coin_change_dp(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1,
                )

    return dp[amount] if dp[amount] != float("inf") else -1
