import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Приводит строку к нормальному виду.

    casefold=True - casefold(), иначе lower().
    yo2e=True - заменяет ё/Ё на е/Е.
    Управляющие символы (\\t, \\r, \\n) становятся пробелами,
    повторяющиеся пробелы схлопываются в один, края обрезаются.
    """
    # сначала регистр, потом ё (иначе Ё останется)
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на слова: \\w+ с возможными дефисами внутри слова.
    """
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Считает частоты: {слово: количество}.
    """
    freq = {}

    for w in tokens:
        freq[w] = freq.get(w, 0) + 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Топ-N по убыванию частоты, при равенстве - по алфавиту слова.
    """
    pairs = sorted(freq.items(), key=lambda p: (-p[1], p[0]))

    return pairs[:n]


if __name__ == "__main__":
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

    # tokenize
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😜 не слово") == ["emoji", "не", "слово"]

    # count_freq + top_n
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert freq2 == {"aa": 2, "bb": 2, "cc": 1}
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
