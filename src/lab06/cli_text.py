import argparse
import sys
 
from src.lib.text import normalize, tokenize, count_freq, top_n
 
 
def cmd_cat(path: str, numbered: bool) -> None:
    """Печатает файл построчно; numbered=True — с номерами строк."""
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if numbered:
                print(f"{i}: {line}")
            else:
                print(line)
 
 
def cmd_stats(path: str, top: int) -> None:
    """Печатает топ-N самых частых слов файла."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    freq = count_freq(tokenize(normalize(text)))
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")
 
 
def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилиты для текста (ЛР6)")
    subparsers = parser.add_subparsers(dest="command", required=True)
 
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
 
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов показать (по умолчанию 5)")
 
    args = parser.parse_args()
 
    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            if args.top <= 0:
                parser.error("--top должен быть больше 0")
            cmd_stats(args.input, args.top)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: файл {args.input} не в кодировке UTF-8", file=sys.stderr)
        sys.exit(1)
 
 
if __name__ == "__main__":
    main()