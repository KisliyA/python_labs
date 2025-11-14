from pathlib import Path
import sys
import os
import csv
import argparse

# Добавляем пути к внешним модулям (адаптируйте под свою структуру)
sys.path.append('/Users/alexk/dev/python_labs/src/lab04')
from io_txt_csv import normalize, tokenize, count_freq, top_n

sys.path.append('/Users/alexk/dev/python_labs/src/lab03/src/lib/pycache')
from text import *

sys.path.append('/Users/alexk/dev/python_labs/src/lab05')
from json_csv import *



def show_statistics(file_path, top_count):
    """
    Выводит топ-N самых частых слов из файла.
    :param file_path: путь к текстовому файлу
    :param top_count: количество слов в топе
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    normalized = normalize(text)
    tokens = tokenize(normalized)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, top_count)
    
    print("Топ-{} слов по частоте:".format(top_count))
    for word, freq in top_words:
        print(f"{word}: {freq}")



def display_content(file_path, with_numbers=False):
    """
    Построчно выводит содержимое файла.
    :param file_path: путь к файлу
    :param with_numbers: если True — нумерует строки
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for idx, line in enumerate(lines, start=1):
        line = line.rstrip()  # убираем \n в конце
        if with_numbers:
            print(f"{idx}: {line}")
        else:
            print(line)



def cli_app():
    """
    Главная функция: настраивает CLI и обрабатывает команды.
    """
    parser = argparse.ArgumentParser(
        description="Утилиты для анализа текста (лабораторная №6)"
    )
    subparsers = parser.add_subparsers(dest="action", help="Доступные команды")

    # Команда 'cat' — вывод содержимого файла
    cat_cmd = subparsers.add_parser("cat", help="Показать содержимое файла")
    cat_cmd.add_argument("--file", required=True, help="Путь к файлу")
    cat_cmd.add_argument("-n", "--number", action="store_true", help="Нумеровать строки")

    # Команда 'stats' — статистика частот слов
    stats_cmd = subparsers.add_parser("stats", help="Анализ частоты слов")
    stats_cmd.add_argument("--file", required=True, help="Путь к файлу")
    stats_cmd.add_argument("--count", type=int, default=5, help="Сколько слов показать в топе")

    args = parser.parse_args()

    if args.action == "cat":
        display_content(args.file, args.number)
    elif args.action == "stats":
        show_statistics(args.file, args.count)
    else:
        parser.print_help()



if name == "main":
    cli_app()