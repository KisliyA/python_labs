import pytest
import sys
import os

sys.path.append("/Users/alexk/dev/python_labs/src/lab03/src/lib")
from text import *


@pytest.mark.parametrize(
    "text, expected",
    [
        ("ПРИВЕТ МИР", "привет мир"),
        ("Ёжик и Ёлка", "ежик и елка"),
        ("Тест 123", "тест 123"),
        ("", ""),
        ("   Много   Пробелов   ", "много пробелов"),
    ],
)
def test_normalize(text, expected):
    assert normalize(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("привет, мир!", ["привет", "мир"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("", []),
        ("   ", []),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["привет", "мир", "привет"], {"привет": 2, "мир": 1}),
        ([], {}),
        (["слово"], {"слово": 1}),
        (["я", "ты", "я", "мы"], {"я": 2, "ты": 1, "мы": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"привет": 5, "мир": 3, "пока": 7}, 2, [("пока", 7), ("привет", 5)]),
        (
            {"яблоко": 3, "банан": 3, "апельсин": 3},
            3,
            [("апельсин", 3), ("банан", 3), ("яблоко", 3)],
        ),
        ({}, 5, []),
        ({"слово": 1}, 1, [("слово", 1)]),
        ({"а": 1, "б": 2}, 10, [("б", 2), ("а", 1)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected
