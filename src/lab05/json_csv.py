import csv
import json
from pathlib import Path
 
 
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл (список словарей) в CSV.
    Отсутствующие поля заполняются пустыми строками.
    Порядок колонок — как в первом объекте, новые ключи добавляются в конец.
    """
    if not json_path.endswith(".json"):
        raise ValueError("нужен .json файл")
    if not Path(json_path).exists():
        raise FileNotFoundError(json_path)
 
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
 
    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    for row in data:
        if not isinstance(row, dict):
            raise ValueError("в списке должны быть только словари")
 
    # все ключи: сначала из первого объекта, потом новые
    fieldnames = []
    for row in data:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
 
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            # нет поля -> пустая строка
            writer.writerow({k: row.get(k, "") for k in fieldnames})
 
 
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    if not csv_path.endswith(".csv"):
        raise ValueError("нужен .csv файл")
    if not Path(csv_path).exists():
        raise FileNotFoundError(csv_path)
 
    with open(csv_path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
 
    if not rows:
        raise ValueError("пустой CSV")
 
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
 
 
if __name__ == "__main__":
    Path("data/out").mkdir(exist_ok=True)
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("готово")