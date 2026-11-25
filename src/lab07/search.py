def linear_search(nums: list[int], x: int) -> int:
    """Возвращает индекс первого вхождения x или -1.

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for index, value in enumerate(nums):
        if value == x:
            return index
    return -1


def binary_search(sorted_nums: list[int], x: int) -> int:
    """Возвращает индекс любого вхождения x в отсортированном списке или -1.

    Список должен быть отсортирован по возрастанию. На неотсортированном
    списке результат не определён.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        value = sorted_nums[mid]
        if value == x:
            return mid
        if value < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """Возвращает индексы i < j, для которых nums[i] + nums[j] == target.

    Перебирает все пары. Если подходящей пары нет, возвращает None.

    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """Решает Two Sum за один проход со словарём.

    При нескольких ответах допустим любой. Если пары нет, возвращает None.
    """
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        if value not in seen:
            seen[value] = index

    return None
