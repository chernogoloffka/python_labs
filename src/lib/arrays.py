def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает (минимум, максимум)."""
    if len(nums) == 0:
        raise ValueError("Список не должен быть пустым")
    minimum = nums[0]
    maximum = nums[0]
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("Нужны только числа")
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum
 
 
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений."""
    for x in nums:
        if not isinstance(x, (int, float)):
            raise TypeError("Нужны только числа")
    unique_nums = list(set(nums))
    for i in range(len(unique_nums)):
        swapped = False
        for j in range(0, len(unique_nums) - i - 1):
            if unique_nums[j] > unique_nums[j + 1]:
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
                swapped = True
        if not swapped:
            break
    return unique_nums
 
 
def flatten(mat: list[list | tuple]) -> list:
    """Расплющивает матрицу в один список по строкам."""
    if not isinstance(mat, (list, tuple)):
        raise TypeError("Нужен список списков")
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Строка должна быть списком или кортежем")
        result.extend(row)
    return result