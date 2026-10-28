import csv
from pathlib import Path
 
from openpyxl import Workbook
 
 
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Первая строка CSV — заголовок. Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    if not csv_path.endswith(".csv"):
        raise ValueError("нужен .csv файл")
    if not Path(csv_path).exists():
        raise FileNotFoundError(csv_path)
 
    with open(csv_path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
 
    if not rows:
        raise ValueError("пустой CSV")
 
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
 
    for row in rows:
        ws.append(row)
 
    # автоширина: длина самого длинного значения в колонке, но не меньше 8
    for column in ws.columns:
        width = max(len(str(cell.value or "")) for cell in column)
        ws.column_dimensions[column[0].column_letter].width = max(width, 8)
 
    wb.save(xlsx_path)
 
 
if __name__ == "__main__":
    Path("data/out").mkdir(exist_ok=True)
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
    print("готово")