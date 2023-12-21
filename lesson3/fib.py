# быстрое вычисление чисел Фибоначчи;
# from memory_profiler import profile
import sys
sys.set_int_max_str_digits(0)
sys.path.append("..")
from shared import timeit


#  @profile
# Top-to-bottom метод с использованием рекурсии
def fib(n):
    def dp(i):
        if i == 0:
            return 0
        if i == 1 or i == 2:
            return 1
        if i not in memo:
            memo[i] = dp(i - 2) + dp(i - 1)
        return memo[i]
    memo = {}
    return dp(n)


# Bottom-to-top метод с использованием итерации
# @profile
def fib_bottom_up(n):
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]


@timeit
def recurrence_fib(count):
    print(fib(count))


@timeit
def bottom_up_fib(count):
    print(fib_bottom_up(count))


if __name__ == "__main__":
    for i in [10, 100, 1000, 10000]:
        print(f"Calculate reccurence fib for {i}")
        recurrence_fib(i)
        print(f"Calculate bottom up fib for {i}")
        bottom_up_fib(i)

    """
    print(f"Recursive fib for {sys.argv[1]}")
    print(recurrence_fib(int(sys.argv[1])))
    print(f"Bottom up fib for {sys.argv[1]}")
    print(bottom_up_fib(int(sys.argv[1])))
    """
