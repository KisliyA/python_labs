from pathlib import Path
import sys
import os
import csv
import argparse

sys.path.append('/Users/alexk/dev/python_labs/src/lab05')
from json_csv import *

sys.path.append('src/lab_05')
from csv_xlsx import *

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    """
        Вызываем функции в зависимости от аргументов.
    """

    match args.cmd:
        case 'json2csv':
            json_to_csv(args.input, args.output)
        case 'csv2json':
            csv_to_json(args.input, args.output)
        case 'csv2xlsx':
            csv_to_xlsx(args.input, args.output)
    print('work')
    input()

main()