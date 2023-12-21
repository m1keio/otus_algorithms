# поиск простых чисел перебором делителей;
import sys

sys.path.append("..")
# pylint: disable=wrong-import-position
# pylint: disable=import-error
from shared import timeit
# from memory_profiler import profile


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True


@timeit
# @profile
def get_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


@timeit
# @profile
def get_primes_odd(n):
    if n < 2:
        return []
    primes = []
    primes.append(2)
    for i in range(1, n + 1, 2):
        if is_prime(i):
            primes.append(i)
    return primes


@timeit
# @profile
def eratosthenes(n):
    if n < 2:
        return []
    # Заполняем список числами от 0 до n
    sieve = list(range(n + 1))
    # 1 нужно заменить на 0 так как она не является простым числом
    sieve[1] = 0
    # итерируемся по списку
    for i in sieve:
        # Если значение y не равно 0 то это простое число,
        # следовательно нужно найти следующие кратные этому числу.
        # начинаем с i+i - это первое кратное, зануляем его и переходи к следующему
        # (i+i)+i - это второе кратное и т.д.
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
        # переходим к следующему не 0 значению в списке sieve
    # удаляем все 0 значения из списка для удобства
    sieve1 = [x for x in sieve if x != 0]
    return sieve1


def main(count):
    print("===================================")
    primes_1 = get_primes(count)
    print(len(primes_1))
    print("===================================")
    primes_2 = get_primes_odd(count)
    print(len(primes_2))
    print("===================================")
    primes_3 = eratosthenes(count)
    print(len(primes_3))


if __name__ == "__main__":
    for i in [10, 100, 10000, 100000]:
        print(f"from 1 to {i}")
        main(i)
