import sys
sys.path.append("..")
from shared import timeit
# from memory_profiler import profile

# memo = {}


# @profile
def power_dumb(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


# @profile
def power_iter(a, n):
    result = 1
    while n:
        # Является ли n нечетным числом (n % 2).
        # Если это так, то result умножается на a и n уменьшается на 1.
        # Пример: 2^5 = 2^4 * 2. n = 5 - 1 = 4.
        if n % 2:
            result *= a
            n -= 1
        # Если n четное, то a умножается на само себя и n делится на 2.
        # Это соответствует случаю, когда степень четная.
        # Пример: 2^4 = 2^2 * 2^2. n = 4 / 2 = 2.
        else:
            a *= a
            n /= 2
    return result


def power(a, n):
    #
    #    функция возвращает 1, так как любое число, возведенное в степень 0, равно 1.
    #
    if n == 0:
        return 1
    #
    #    Если степень n нечетная (то есть n % 2 == 1), функция рекурсивно вызывает себя с n - 1
    #    и умножает результат на a. Это работает, потому что a^n = a^(n-1) * a.
    #
    elif n % 2 == 1:
        return power(a, n - 1) * a
    #
    #    Если степень n четная, функция рекурсивно вызывает себя дважды с n / 2
    #    и умножает результаты. Это работает, потому что a^n = a^(n/2) * a^(n/2).
    #
    else:
        return power(a, n / 2) * power(a, n / 2)


def power_memo(a, n, memo={}):
    #
    #    Если степень n уже вычислена, она возвращается из словаря.
    #
    if n in memo:
        return memo[n]
    #
    #    функция возвращает 1, так как любое число, возведенное в степень 0, равно 1.
    #
    if n == 0:
        return 1
    #
    #    Если степень n нечетная (то есть n % 2 == 1), функция рекурсивно вызывает себя с n - 1
    #    и умножает результат на a. Это работает, потому что a^n = a^(n-1) * a.
    #
    elif n % 2 == 1:
        memo[n] = power(a, n - 1) * a
        return memo[n]
    #
    #    Если степень n четная, функция рекурсивно вызывает себя дважды с n / 2
    #    и умножает результаты. Это работает, потому что a^n = a^(n/2) * a^(n/2).
    #
    else:
        memo[n] = power(a, n / 2) * power(a, n / 2)
        return memo[n]


@timeit
def reg_power_dumb(base, dpower):
    return power_dumb(base, dpower)


@timeit
def reg_power_iter(base, dpower):
    return power_iter(base, dpower)


@timeit
# @profile
def fast_power(base, dpower):
    return power(base, dpower)


@timeit
# @profile
def fast_power_memo(base, dpower):
    memo = {}
    return power_memo(base, dpower, memo)


if __name__ == "__main__":
    base = float(sys.argv[1])
    dpower = int(sys.argv[2])
    print(f"^^^^^ reg power dumb: {reg_power_dumb(base, dpower)}")
    print(f"^^^^^ reg power iter: {reg_power_iter(base, dpower)}")
    print(f"^^^^^ fast power: {fast_power(base, dpower)}")
    print(f"^^^^^ fast power memo: {fast_power_memo(base, dpower)}")
