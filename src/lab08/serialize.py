import json
from pathlib import Path

from src.lab08.models import student_from_dict, student_to_dict


def students_to_json(students: list[dict], path: str | Path) -> None:
    """Проверяет записи и сохраняет их как массив объектов JSON."""
    data = [student_to_dict(student) for student in students]
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def students_from_json(path: str | Path) -> list[dict]:
    """Читает JSON-массив; первая битая запись вызывает ValueError."""
    input_path = Path(path)
    with input_path.open(encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("JSON: корневой элемент должен быть массивом записей")

    students = []
    for index, item in enumerate(data, start=1):
        try:
            student = student_from_dict(item)
        except ValueError as exc:
            raise ValueError(f"JSON: ошибка в записи {index}: {exc}") from exc
        students.append(student)

    return students
