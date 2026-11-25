from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def make_student(fio: str, birthdate: str, group: str, gpa: int | float) -> dict:
    """Создаёт запись Student, проверяет поля и нормализует значения."""
    record = {
        "fio": fio,
        "birthdate": birthdate,
        "group": group,
        "gpa": gpa,
    }
    validate_student(record)
    record["fio"] = record["fio"].strip()
    record["group"] = record["group"].strip()
    record["gpa"] = float(record["gpa"])
    return record


def validate_student(rec: dict) -> None:
    """Проверяет точный набор ключей и все значения записи Student."""
    if not isinstance(rec, dict):
        raise ValueError("Student: запись должна быть словарём")

    expected_keys = set(STUDENT_FIELDS)
    actual_keys = set(rec)
    if actual_keys != expected_keys:
        missing = sorted(expected_keys - actual_keys)
        extra = sorted(actual_keys - expected_keys, key=str)
        raise ValueError(
            f"Student: неверный набор ключей; отсутствуют {missing}, лишние {extra}"
        )

    for field in ("fio", "group"):
        if not isinstance(rec[field], str) or not rec[field].strip():
            raise ValueError(f"{field}: значение должно быть непустой строкой")

    if not isinstance(rec["birthdate"], str):
        raise ValueError("Неверный формат даты")

    try:
        birth_date = date.fromisoformat(rec["birthdate"])
    except ValueError as exc:
        raise ValueError("Неверный формат даты") from exc

    if birth_date.isoformat() != rec["birthdate"]:
        raise ValueError("Неверный формат даты")
    if birth_date > date.today():
        raise ValueError("Не может быть в будущем")

    gpa = rec["gpa"]
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError("Неверный формат GPA")
    if not 0 <= gpa <= 5:
        raise ValueError("Неверный формат GPA")


def student_age(rec: dict, today: date | None = None) -> int:
    """Возвращает полное количество лет на дату today или на сегодня."""
    validate_student(rec)
    birth_date = date.fromisoformat(rec["birthdate"])
    if today is None:
        today = date.today()
    if not isinstance(today, date):
        raise ValueError("today: ожидается объект datetime.date")
    if birth_date > today:
        raise ValueError("birthdate: дата рождения позже даты расчёта возраста")

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def format_student(rec: dict) -> str:
    """Форматирует запись как 'Иванов И.И. (группа), 19 лет, GPA 4.30'."""
    validate_student(rec)
    parts = rec["fio"].split()
    surname = parts[0]
    initials = "".join(f"{part[0].upper()}." for part in parts[1:])
    short_fio = f"{surname} {initials}" if initials else surname
    return (
        f"{short_fio} ({rec['group']}), {student_age(rec)} лет, "
        f"GPA {float(rec['gpa']):.2f}"
    )


def student_to_dict(rec: dict) -> dict:
    """Возвращает новую независимую копию записи для сериализации."""
    validate_student(rec)
    copy = {field: rec[field] for field in STUDENT_FIELDS}
    copy["gpa"] = float(copy["gpa"])
    return copy


def student_from_dict(d: dict) -> dict:
    """Создаёт валидную запись из словаря и приводит gpa к float."""
    validate_student(d)
    return make_student(
        fio=d["fio"],
        birthdate=d["birthdate"],
        group=d["group"],
        gpa=float(d["gpa"]),
    )
