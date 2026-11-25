import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> None:
    """Сравнивает сортировку с sorted и проверяет неизменность входа."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)

        assert result == sorted(nums), (
            f"{fn.__name__} ошиблась на {nums}: получено {result}, "
            f"ожидалось {sorted(nums)}"
        )
        assert nums == original, f"{fn.__name__} изменила исходный список {original}"


def check_search() -> None:
    """Проверяет поиск на случайных списках, включая крайние элементы."""
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        sorted_nums = sorted(nums)
        targets = [random.randint(-100, 100)]

        if nums:
            targets.extend([nums[0], nums[-1], sorted_nums[0], sorted_nums[-1]])
        else:
            targets.append(0)

        for x in targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1

            linear_result = linear_search(nums, x)
            assert linear_result == expected, (
                f"linear_search({nums}, {x}) вернула {linear_result}, "
                f"ожидалось {expected}"
            )

            binary_result = binary_search(sorted_nums, x)
            if expected == -1:
                assert binary_result == -1, (
                    f"binary_search({sorted_nums}, {x}) вернула {binary_result}, "
                    "ожидалось -1"
                )
            else:
                assert 0 <= binary_result < len(sorted_nums), (
                    f"binary_search({sorted_nums}, {x}) вернула неверный индекс "
                    f"{binary_result}"
                )
                assert sorted_nums[binary_result] == x, (
                    f"binary_search({sorted_nums}, {x}) вернула индекс "
                    f"{binary_result} другого значения"
                )


def check_two_sum(trials: int = 100) -> None:
    """Сверяет оба решения Two Sum и корректность возвращённых индексов."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)
        brute_result = two_sum_brute(nums, target)
        fast_result = two_sum_fast(nums, target)

        assert (brute_result is None) == (fast_result is None), (
            f"Расхождение на nums={nums}, target={target}: "
            f"brute={brute_result}, fast={fast_result}"
        )

        for name, result in (("brute", brute_result), ("fast", fast_result)):
            if result is not None:
                assert isinstance(result, tuple) and len(result) == 2, (
                    f"{name} вернул не пару индексов: {result}; "
                    f"nums={nums}, target={target}"
                )
                i, j = result
                assert 0 <= i < j < len(nums), (
                    f"{name} вернул неверные индексы {result}; "
                    f"nums={nums}, target={target}"
                )
                assert nums[i] + nums[j] == target, (
                    f"{name} вернул пару с неправильной суммой {result}; "
                    f"nums={nums}, target={target}"
                )


if __name__ == "__main__":
    random.seed(42)
    for sort_fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(sort_fn)
    check_search()
    check_two_sum()
    print("OK: 500 проверок (300 сортировок, 100 поисков, 100 Two Sum)")
