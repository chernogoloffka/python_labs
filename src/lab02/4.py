def format_record(rec):
    fio, group, gpa = rec
    parts = fio.split()
    if len(parts) < 2 or len(parts) > 3:
        raise ValueError("ФИО должно содержать 2 или 3 слова")
    group = " ".join(group.split())
    if group == "":
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть от 0 до 5")
    surname = parts[0]
    initials = ""
    for name in parts[1:]:
        initials += name[0].upper() + "."
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"