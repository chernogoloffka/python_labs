import csv
from pathlib import Path
 
 
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает файл целиком и возвращает его содержимое одной строкой.
    Пустой файл -> пустая строка "".
 
    Нет файла -> FileNotFoundError, не та кодировка -> UnicodeDecodeError.
    Другую кодировку можно передать параметром:
        read_text("data/input.txt", encoding="cp1251")
    """
    with open(path, encoding=encoding) as f:
        return f.read()
 
 
def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт папку для файла, если её нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
 
 
def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Записывает строки rows в CSV (разделитель ",").
    Если передан header, он пишется первой строкой.
    Все строки должны быть одной длины, иначе ValueError.
    """
    for row in rows:
        if len(row) != len(rows[0]):
            raise ValueError(f"строки разной длины: {row}")
 
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)