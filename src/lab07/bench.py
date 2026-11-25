import csv
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

DATA_DIR = Path("data/samples/lab07")
OUTPUT_PATH = Path("data/lab07/bench.csv")
SORT_SIZES = (1_000, 10_000, 100_000)
TWO_SUM_SIZES = (1_000, 10_000)


def read_numbers(path: str | Path) -> list[int]:
    """Читает числа из CSV-файла с колонкой value."""
    with open(path, encoding="utf-8") as file:
        return [int(row["value"]) for row in csv.DictReader(file)]


def prepare_numbers(n: int) -> list[int]:
    """Загружает общий набор данных или создаёт его с random.seed(42)."""
    path = DATA_DIR / f"numbers_{n}.csv"
    if path.exists():
        return read_numbers(path)

    random.seed(42)
    numbers = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
    write_csv([(value,) for value in numbers], path, header=("value",))
    return numbers


def bench_sorts(n: int) -> list[tuple]:
    """Измеряет sorted и три собственные сортировки на одних данных."""
    data = prepare_numbers(n)
    rows = []

    seconds = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", seconds))

    for fn in (bubble_sort, insertion_sort, selection_sort):
        if n == 100_000:
            rows.append(("sort", n, fn.__name__, ">60"))
            continue
        seconds = timeit.timeit(lambda: fn(data), number=1)
        rows.append(("sort", n, fn.__name__, seconds))

    return rows


def bench_search() -> list[tuple]:
    """Сравнивает 10 000 линейных и бинарных поисков на 100 000 числах."""
    n = 100_000
    query_count = 10_000
    data = prepare_numbers(n)
    random.seed(42)
    queries = [random.choice(data) for _ in range(query_count)]
    rows = []

    seconds = timeit.timeit(
        lambda: [linear_search(data, x) for x in queries], number=1
    )
    rows.append(("search", n, "linear_search", seconds))

    seconds = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort_for_search", n, "sorted", seconds))

    sorted_data = sorted(data)
    seconds = timeit.timeit(
        lambda: [binary_search(sorted_data, x) for x in queries], number=1
    )
    rows.append(("search", n, "binary_search", seconds))

    return rows


def bench_two_sum(n: int) -> list[tuple]:
    """Сравнивает решения Two Sum; искомая пара гарантированно существует."""
    data = prepare_numbers(n)
    left = n // 3
    right = 2 * n // 3
    target = data[left] + data[right]
    rows = []

    for fn in (two_sum_brute, two_sum_fast):
        seconds = timeit.timeit(lambda: fn(data, target), number=1)
        rows.append(("two_sum", n, fn.__name__, seconds))

    return rows


def print_table(rows: list[tuple]) -> None:
    """Печатает результаты с выровненными колонками."""
    print(f"{'task':<16} {'n':>7} {'impl':<18} {'seconds':>12}")
    print("-" * 58)
    for task, n, impl, seconds in rows:
        seconds_text = f"{seconds:.6f}" if isinstance(seconds, float) else seconds
        print(f"{task:<16} {n:>7} {impl:<18} {seconds_text:>12}")


def main() -> None:
    """Выполняет все замеры, печатает таблицу и сохраняет её в CSV."""
    random.seed(42)
    rows = []

    for n in SORT_SIZES:
        rows.extend(bench_sorts(n))

    rows.extend(bench_search())
    for n in TWO_SUM_SIZES:
        rows.extend(bench_two_sum(n))

    print_table(rows)
    write_csv(rows, OUTPUT_PATH, header=("task", "n", "impl", "seconds"))
    print(f"\nРезультаты сохранены в {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
