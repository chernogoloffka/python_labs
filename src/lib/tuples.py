def format_record(rec: tuple[str, str, float]) -> str:
    """Возвращает строку вида: Иванов И.И., гр. BIVT-25, GPA 4.60"""
    if not isinstance(rec, tuple):
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("В записи должно быть 3 поля")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio и group должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("gpa должен быть числом")
    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")
    parts = fio.split()
    if len(parts) != 2 and len(parts) != 3:
        raise ValueError("Нужны Фамилия Имя [Отчество]")
    group = " ".join(group.split())
    if group == "":
        raise ValueError("Группа не должна быть пустой")
    initials = ""
    for name in parts[1:]:
        initials += name[0].upper() + "."
    return f"{parts[0]} {initials}, гр. {group}, GPA {gpa:.2f}"