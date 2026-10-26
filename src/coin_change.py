def coin_change_recursive(coins, amount):
    # No coins are needed to make an amount of zero.
    if amount == 0:
        return 0
    # A negative amount cannot be made with the available coins.
    if amount < 0:
        return float("inf")

    best = float("inf")
    # Try using each coin and keep the result with the fewest coins.
    for coin in coins:
        best = min(best, coin_change_recursive(coins, amount - coin))

    return best + 1 if best != float("inf") else -1


def coin_change_memoized(coins, amount, memo=None):
    # Create the cache for the first call.
    if memo is None:
        memo = {}

    # Handle base cases before checking or updating the cache.
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")
    if amount in memo:
        return memo[amount]

    best = float("inf")
    # Reuse cached results to avoid solving the same amount repeatedly.
    for coin in coins:
        best = min(best, coin_change_memoized(coins, amount - coin, memo))

    memo[amount] = best + 1 if best != float("inf") else -1
    return memo[amount]


def coin_change_dp(coins, amount):
    # dp[i] stores the minimum coins needed to make amount i.
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    # Build solutions from smaller amounts to larger amounts.
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1,
                )

    return dp[amount] if dp[amount] != float("inf") else -1
