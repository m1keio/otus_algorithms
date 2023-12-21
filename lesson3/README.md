# Возведение в степень

Мы попробовали линейное, рекурсивное, итеративное, и рекурсивное с мемоизацией решение.
Выводы:

1. Линейное решение довольно медленное
2. Рекурсивное решение без мемоизации быстро упирается в лимит рекурсивных вызовов
3. Рекурсивное решение с мемоизацией работает неплохо но на тестах после 10 использует все 32ГБ памяти.

```bash
lesson3(main) ✗: python3 power.py 10 10
'reg_power_dumb'  0.0026 ms
^^^^^ reg power dumb: 10000000000.0
'reg_power_iter'  0.0086 ms
^^^^^ reg power iter: 10000000000.0
'fast_power'  0.0064 ms
^^^^^ fast power: 10000000000.0
'fast_power_memo'  0.0033 ms
^^^^^ fast power memo: 10000000000.0

lesson3(main) ✗: python3 power.py 1.01 100
'reg_power_dumb'  0.0138 ms
^^^^^ reg power dumb: 2.7048138294215294
'reg_power_iter'  0.0310 ms
^^^^^ reg power iter: 2.704813829421529
'fast_power'  0.1314 ms
^^^^^ fast power: 2.7048138294215223
'fast_power_memo'  0.0846 ms
^^^^^ fast power memo: 2.7048138294215223

lesson3(main) ✗: python3 power.py 1.001 1000
'reg_power_dumb'  0.0255 ms
^^^^^ reg power dumb: 2.7169239322355985
'reg_power_iter'  0.0038 ms
^^^^^ reg power iter: 2.7169239322355203
'fast_power'  0.1786 ms
^^^^^ fast power: 2.7169239322355017
'fast_power_memo'  0.1669 ms
^^^^^ fast power memo: 2.7169239322355017

lesson3(main) ✗: python3 power.py 1.0001 10000
'reg_power_dumb'  0.2005 ms
^^^^^ reg power dumb: 2.7181459268248984
'reg_power_iter'  0.0095 ms
^^^^^ reg power iter: 2.718145926824356
'fast_power'  2.1610 ms
^^^^^ fast power: 2.718145926824389
'fast_power_memo'  2.1033 ms
^^^^^ fast power memo: 2.718145926824389
```

# Числа Фибоначчи

Мы попробовали top-to-bottom и bottom-to-top решения.
Выводы:

1. Скорость работы алгоритмов примерно одинаковая. Однако рекурсия опять вызывает проблемы при большой глубине стека вызовов.

```bash
python3 fib.py 100
Calculate reccurence fib for 10
55
'recurrence_fib'  0.0095 ms
Calculate bottom up fib for 10
55
'bottom_up_fib'  0.0043 ms
Calculate reccurence fib for 100
354224848179261915075
'recurrence_fib'  0.0317 ms
Calculate bottom up fib for 100
354224848179261915075
'bottom_up_fib'  0.0091 ms
Calculate reccurence fib for 1000
43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
'recurrence_fib'  0.4432 ms
Calculate bottom up fib for 1000
43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
'bottom_up_fib'  0.0777 ms
Calculate reccurence fib for 10000
Traceback (most recent call last):
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 49, in <module>
    recurrence_fib(i)
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/../shared/__init__.py", line 7, in timed
    result = method(*args, **kw)
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 38, in recurrence_fib
    print(fib(count))
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 21, in fib
    return dp(n)
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 18, in dp
    memo[i] = dp(i - 2) + dp(i - 1)
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 18, in dp
    memo[i] = dp(i - 2) + dp(i - 1)
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 18, in dp
    memo[i] = dp(i - 2) + dp(i - 1)
  [Previous line repeated 992 more times]
  File "/home/mtiurin/private/git/otus_algorithms/lesson3/fib.py", line 13, in dp
    if i == 0:
RecursionError: maximum recursion depth exceeded in comparison
```

# Прострые числа

Мы попробовали линейный перебор, перебор только четных и решето Эратосфена.
Выводы:

1. Решето обгоняет остальные решения по скорости.
2. Вариации исключения частей изначальное последовательности не дают значимого прироста.

```bash
from 1 to 10
===================================
'get_primes'  0.0048 ms
4
===================================
'get_primes_odd'  0.0024 ms
4
===================================
'eratosthenes'  0.0036 ms
4
from 1 to 100
===================================
'get_primes'  0.0353 ms
25
===================================
'get_primes_odd'  0.0391 ms
25
===================================
'eratosthenes'  0.0169 ms
25
from 1 to 10000
===================================
'get_primes'  140.5468 ms
1229
===================================
'get_primes_odd'  131.9020 ms
1229
===================================
'eratosthenes'  1.0765 ms
1229
from 1 to 100000
===================================
'get_primes'  11294.6956 ms
9592
===================================
'get_primes_odd'  10711.2026 ms
9592
===================================
'eratosthenes'  11.3549 ms
9592
```
