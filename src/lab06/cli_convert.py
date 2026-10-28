import argparse
import sys
from pathlib import Path
 
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
 
 
def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных (ЛР6)")
    sub = parser.add_subparsers(dest="cmd", required=True)
 
    p1 = sub.add_parser("json2csv", help="JSON -> CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной .json")
    p1.add_argument("--out", dest="output", required=True, help="Выходной .csv")
 
    p2 = sub.add_parser("csv2json", help="CSV -> JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной .csv")
    p2.add_argument("--out", dest="output", required=True, help="Выходной .json")
 
    p3 = sub.add_parser("csv2xlsx", help="CSV -> XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной .csv")
    p3.add_argument("--out", dest="output", required=True, help="Выходной .xlsx")
 
    args = parser.parse_args()
 
    # создать папку для результата, если её нет (например, data/out)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
 
    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден: {e.filename or e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
 
    print(f"Готово: {args.input} -> {args.output}")
 
 
if __name__ == "__main__":
    main()