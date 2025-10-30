import text

def test_normalize_casefold_and_spaces():
    s = "ПрИвЕт\nМИр\t"
    assert text.normalize(s) == "привет мир"


def test_normalize_yo2e():
    s = "ёжик, Ёлка"
    assert text.normalize(s) == "ежик, елка"


def test_normalize_crlf():
    s = "Hello\r\nWorld"
    assert text.normalize(s) == "hello world"


def test_normalize_double_spaces():
    s = "  двойные   пробелы  "
    assert text.normalize(s) == "двойные пробелы"


def test_tokenize_simple_ru():
    assert text.tokenize("привет мир") == ["привет", "мир"]


def test_tokenize_punct():
    assert text.tokenize("hello,world!!!") == ["hello", "world"]


def test_tokenize_hyphen():
    assert text.tokenize("по-настоящему круто") == ["по-настоящему", "круто"]


def test_tokenize_numbers():
    assert text.tokenize("2025 год") == ["2025", "год"]


def test_tokenize_emoji_filtered():
    assert text.tokenize("emoji 😃 не слово") == ["emoji", "не", "слово"]


def test_count_freq_and_top_n_basic():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = text.count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert text.top_n(freq, n=2) == [("a", 3), ("b", 2)]


def test_top_n_tie_alpha_sort():
    tokens = ["bb", "aa", "bb", "aa", "cc"]
    freq = text.count_freq(tokens)
    assert freq == {"aa": 2, "bb": 2, "cc": 1}
    assert text.top_n(freq, n=2) == [("aa", 2), ("bb", 2)]