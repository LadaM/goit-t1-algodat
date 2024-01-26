import timeit
from functools import lru_cache


def with_time_measure(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()  # Start the timer
        res = func(*args, **kwargs)
        end = timeit.default_timer()  # Stop the timer
        print(f"Total time: {1000 * (end - start): .10f} ms")
        return res

    return wrapper


def fibonacci(n):
    if n <= 1:  # base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive case


@with_time_measure
def call_fibonacci(n):
    return fibonacci(n)


@with_time_measure
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = value
        return value


@with_time_measure
def call_fibonacci_memo(n):
    return fibonacci_memo(n)


@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci_memo_lru(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memo_lru(n - 1) + fibonacci_memo_lru(n - 2)


@with_time_measure
def call_fibonacci_memo_lru(n):
    return fibonacci_memo_lru(n)


def compare_fibonacci_algorithms(n):
    print(f"{'Recursive':<10}", end=" --> ")
    call_fibonacci(n)
    print(f"{'Iterative':<10}", end=" --> ")
    fibonacci_iterative(n)
    print(f"{'Memo':<10}", end=" --> ")
    call_fibonacci_memo(n)
    print(f"{'Memo LRU':<10}", end=" --> ")
    call_fibonacci_memo_lru(n)


if __name__ == "__main__":
    # print(f"{fibonacci(10)} = {fibonacci_iterative(10)}") # Output: 55
    compare_fibonacci_algorithms(
        41
    )  # with n=41 recursive call takes a bit less than 30sec
