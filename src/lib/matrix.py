def check_rectangular(mat) -> None:
    """Проверяет, что mat — прямоугольная матрица."""
    if not isinstance(mat, (list, tuple)):
        raise TypeError("Нужен список списков")
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Строка должна быть списком")
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError("Строки разной длины")
 
 
def transpose(mat: list[list[float | int]]) -> list[list]:
    """Меняет строки и столбцы местами."""
    check_rectangular(mat)
    if len(mat) == 0:
        return []
    result = []
    for j in range(len(mat[0])):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result
 
 
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке."""
    check_rectangular(mat)
    if len(mat) == 0:
        raise ValueError("Матрица пуста")
    result = []
    for row in mat:
        s = 0
        for x in row:
            s += x
        result.append(s)
    return result
 
 
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждому столбцу."""
    check_rectangular(mat)
    if len(mat) == 0:
        raise ValueError("Матрица пуста")
    result = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        result.append(s)
    return result