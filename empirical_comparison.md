## Empirical Comparison

The three implementations were tested with coin denominations `[1, 2, 5]` and target amounts from 5 through 25. I used a `benchmark.py` file in the `src` directory, imported the coin-change function and `perf_counter`, and ran it with `python3 benchmark.py`. The elapsed time was converted to milliseconds. The results below were collected on macOS; exact times may vary depending on the computer and system load.

| Amount | Naive recursive (ms) | Memoized (ms) | Bottom-up DP (ms) |
| -----: | -------------------: | ------------: | ----------------: |
|      5 |               0.0206 |        0.0037 |            0.0034 |
|     10 |               0.0436 |        0.0037 |            0.0022 |
|     15 |               0.5985 |        0.0048 |            0.0026 |
|     20 |               7.8215 |        0.0064 |            0.0030 |
|     25 |             119.5576 |        0.0121 |            0.0063 |

The naive recursive approach becomes much slower as the amount increases because it repeatedly solves the same subproblems. Memoization avoids this repeated work by storing previously computed results, making its runtime nearly constant for this small test. The bottom-up dynamic programming approach was the fastest overall because it calculates each amount iteratively and avoids function-call overhead. These results demonstrate why dynamic programming is preferable for larger coin-change amounts.