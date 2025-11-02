"""
Завдання 2: generator_numbers + sum_profit
Витягує числа, відокремлені пробілами, та підсумовує (генератор + функція-аргумент).
"""

import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Ітерує по всіх числах у тексті (цілі або дробові з крапкою), які чітко
    відокремлені пробілами або межами рядка.
    """
    pattern = r'(?:(?<=\s)|^)(\d+(?:\.\d+)?)(?=(?:\s)|$)'
    for m in re.finditer(pattern, text):
        yield float(m.group(1))


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return round(sum(func(text)), 2)


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
