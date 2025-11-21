import pytest
import json
import csv
import sys
import os

sys.path.append("/Users/alexk/dev/python_labs/src/lab05")
from json_csv import *
from csv_xlsx import *


def test_json_to_csv_correct(tmp_path):
    """Правильная конвертация JSON в CSV"""
    # Создаем JSON файл
    json_file = tmp_path / "test.json"
    data = [{"name": "Иван", "age": 25}, {"name": "Мария", "age": 30}]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    # Конвертируем
    csv_file = tmp_path / "test.csv"
    json_to_csv(str(json_file), str(csv_file))

    # Проверяем
    assert csv_file.exists()

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "Иван"
    assert rows[1]["name"] == "Мария"


def test_csv_to_json_correct(tmp_path):
    """Правильная конвертация CSV в JSON"""
    # Создаем CSV файл
    csv_file = tmp_path / "test.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Петр", "age": "35"})
        writer.writerow({"name": "Анна", "age": "28"})

    # Конвертируем
    json_file = tmp_path / "test.json"
    csv_to_json(str(csv_file), str(json_file))

    # Проверяем
    assert json_file.exists()

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Петр"
    assert data[1]["name"] == "Анна"


def test_json_to_csv_empty_file(tmp_path):
    """Ошибка при пустом JSON файле"""
    json_file = tmp_path / "empty.json"
    json_file.write_text("", encoding="utf-8")

    csv_file = tmp_path / "test.csv"

    with pytest.raises(ValueError):
        json_to_csv(str(json_file), str(csv_file))


def test_csv_to_json_empty_file(tmp_path):
    """Ошибка при пустом CSV файле"""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("", encoding="utf-8")

    json_file = tmp_path / "test.json"

    with pytest.raises(ValueError):
        csv_to_json(str(csv_file), str(json_file))


def test_json_to_csv_wrong_path():
    """Ошибка при несуществующем JSON файле"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("нет_такого_файла.json", "test.csv")


def test_csv_to_json_wrong_path():
    """Ошибка при несуществующем CSV файле"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("нет_такого_файла.csv", "test.json")
