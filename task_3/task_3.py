"""
Завдання 3 (не обов'язкове): аналіз логів (CLI)
Функції: parse_log_line, load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts.
"""

import argparse
from collections import Counter
from typing import Dict, List, Optional


def parse_log_line(line: str) -> Dict[str, str]:
    parts = line.strip().split()
    if len(parts) < 4:
        raise ValueError("Неправильний формат лог-рядка")
    date, time, level = parts[0], parts[1], parts[2]
    message = " ".join(parts[3:])
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs: List[Dict[str, str]] = []
    with open(file_path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                logs.append(parse_log_line(line))
            except ValueError:
                continue
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    level_up = level.upper()
    return [rec for rec in logs if rec.get("level", "").upper() == level_up]


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    return dict(Counter(rec.get("level", "") for rec in logs))


def display_log_counts(counts: Dict[str, int]) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in ("INFO", "DEBUG", "ERROR", "WARNING"):
        print(f"{level:<16} | {counts.get(level, 0)}")


def main(argv: Optional[list] = None) -> None:
    parser = argparse.ArgumentParser(description="Аналізатор логів")
    parser.add_argument("file", help="Шлях до лог-файлу")
    parser.add_argument("level", nargs="?", help="(необов'язково) рівень: info|error|debug|warning")
    args = parser.parse_args(argv)

    try:
        logs = load_logs(args.file)
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return
    except OSError as e:
        print(f"Помилка читання файлу: {e}")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if args.level:
        lvl = args.level.upper()
        filtered = filter_logs_by_level(logs, lvl)
        print(f"\nДеталі логів для рівня '{lvl}':")
        for rec in filtered:
            print(f"{rec['date']} {rec['time']} - {rec['message']}")


if __name__ == "__main__":
    main()
