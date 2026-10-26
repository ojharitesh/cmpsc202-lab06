from time import perf_counter
from coin_change import coin_change_recursive

coins = [1, 2, 5]
amount = 10

start = perf_counter()
coin_change_recursive(coins, amount)
end = perf_counter()

print((end - start) * 1000, "ms")
