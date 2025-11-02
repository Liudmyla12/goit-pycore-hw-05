"""
Завдання 1: caching_fibonacci (замикання + рекурсія + кеш)
"""

from typing import Dict


def caching_fibonacci():
    """
    Повертає внутрішню функцію fibonacci(n), яка використовує кеш у замиканні.
    """
    cache: Dict[int, int] = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        if n < 0:
            raise ValueError("n має бути невід'ємним цілим числом")
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))  # 55
    print(fib(15))  # 610
