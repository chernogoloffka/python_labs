def bubble_sort(nums: list[int]) -> list[int]:
    """Возвращает новый список, отсортированный по возрастанию.

    Исходный список не изменяется. Флаг swapped позволяет завершить работу
    раньше, если за проход не было ни одного обмена.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    result = list(nums)

    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break

    return result


def insertion_sort(nums: list[int]) -> list[int]:
    """Возвращает новый отсортированный список, не изменяя исходный."""
    result = list(nums)

    for index in range(1, len(result)):
        current = result[index]
        position = index - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result


def selection_sort(nums: list[int]) -> list[int]:
    """Возвращает новый отсортированный список, не изменяя исходный."""
    result = list(nums)

    for index in range(len(result) - 1):
        min_index = index
        for candidate in range(index + 1, len(result)):
            if result[candidate] < result[min_index]:
                min_index = candidate

        if min_index != index:
            result[index], result[min_index] = result[min_index], result[index]

    return result
