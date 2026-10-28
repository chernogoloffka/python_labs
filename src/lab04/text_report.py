import sys
 
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n
 
IN_PATH = "data/lab04/input.txt"
OUT_PATH = "data/lab04/report.csv"
 
 
def main() -> None:
    try:
        text = read_text(IN_PATH)
    except FileNotFoundError:
        print(f"Ошибка: файл {IN_PATH} не найден", file=sys.stderr)
        sys.exit(1)
 
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
 
    # count по убыванию, при равенстве word по алфавиту
    rows = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    write_csv(rows, OUT_PATH, header=("word", "count"))
 
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")
 
 
if __name__ == "__main__":
    main()