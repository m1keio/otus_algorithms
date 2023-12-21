import time
import sys


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.4f ms' %
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


""" Problem: Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


@timeit
def climbStairs(n: int) -> int:
    def dp(i):
        """A function that returns the answer to the problem for a given state."""
        # Base cases: when i is less than 3 there are i ways to reach the ith stair.
        if i <= 2:
            return i

        # If i is not a base case, then use the recurrence relation.
        return dp(i - 1) + dp(i - 2)

    return dp(n)


@timeit
def climbStairsWithMemo(n: int) -> int:
    def dp(i):
        """A function that returns the answer to the problem for a given state."""
        # Base cases: when i is less than 3 there are i ways to reach the ith stair.
        if i <= 2:
            return i

        # If i is not a base case, then use the recurrence relation.
        if i not in memo:
            memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]
    memo = {}
    return dp(n)


@timeit
def climbStairsBottomTop(n: int) -> int:
    if n == 1:
        return 1

    # An array that represents the answer to the problem for a given state
    dp = [0] * (n + 1)
    dp[1] = 1  # Base cases
    dp[2] = 2  # Base cases

    for i in range(3, n + 1):
        print(f"{dp[i - 1]}  {dp[i - 2]})")
        dp[i] = dp[i - 1] + dp[i - 2]  # Recurrence relation

    return dp[n]


num = int(sys.argv[1])

print(climbStairs(num))
print(climbStairsWithMemo(num))
print(climbStairsBottomTop(num))
