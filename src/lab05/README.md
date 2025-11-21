<h1>Программирование и алгоритмизация (Лабораторные)</h1>

<h2>Лабораторная №1:</h2>

**Задание №1:**
```python
from pathlib import Path
import json, csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    '''JSON-CSV'''
    j_path = Path(json_path)

    if not j_path.exists():
        raise FileNotFoundError('Файл не найден')
    if j_path.suffix != '.json':
        raise ValueError("Неверный тип файла")
    
    with open(j_path, 'r', encoding='utf-8') as j_file:
        try:
            j_data = json.load(j_file)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
        if not j_data:
            raise ValueError('Файл JSON пуст')
        if not isinstance(j_data, list):
            raise ValueError('Файл не является СПИСКОМ словарей')
        if not all(isinstance(row, dict) for row in j_data):
            raise ValueError('Файл не является списком СЛОВАРЕЙ')
    
    # Все ключи в алфавитном порядке + заполнение пустых полей
    all_fields = sorted(set(key for item in j_data for key in item.keys()))
    
    c_path = Path(csv_path)
    c_path.parent.mkdir(parents=True, exist_ok=True)  # Создаем директорию
    
    with open(c_path, 'w', encoding='utf-8', newline='') as c_file:
        c_writer = csv.DictWriter(c_file, fieldnames=all_fields)
        c_writer.writeheader()
        for row in j_data:
            # Заполняем отсутствующие поля пустыми строками
            complete_row = {field: row.get(field, '') for field in all_fields}
            c_writer.writerow(complete_row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    ''' CSV-JSON-'''
    c_path = Path(csv_path)

    if not c_path.exists():
        raise FileNotFoundError('Файл не найден')
    if c_path.suffix != '.csv':
        raise ValueError("Неверный тип файла")
    
    with open(c_path, 'r', encoding='utf-8') as c_file:
        c_data = csv.DictReader(c_file)
        if not c_data.fieldnames:
            raise ValueError('Файл пустой или в нем нет заголовков')
        c_rows = list(c_data)
        if not c_rows:
            raise ValueError('В файле есть заголовки, но нет данных')
        
    j_path = Path(json_path)
    j_path.parent.mkdir(parents=True, exist_ok=True)  # Создаем директорию
    
    with open(j_path, 'w', encoding='utf-8') as j_file:
        json.dump(c_rows, j_file, ensure_ascii=False, indent=2)
```
![exe1!](/images/lab05/json_csv.png)
-------------------------------------------
**Задание №2:**
```python
# src/lab05/csv_xlsx.py
i# src/lab05/csv_xlsx.py
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    try:
        if not Path(csv_path).exists():
            raise FileNotFoundError(f"Файл не найден: {csv_path}")
        
        # Чтение CSV
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        if not rows:
            raise ValueError("CSV файл пуст")
        
        try:
            from openpyxl import Workbook
            from openpyxl.utils import get_column_letter
        except ImportError:
            raise ImportError("Требуется установить openpyxl: pip install openpyxl")
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        
        # Запись данных
        for row_idx, row in enumerate(rows, 1):
            for col_idx, value in enumerate(row, 1):
                ws.cell(row=row_idx, column=col_idx, value=value)
        
        # колонki автоширина
        for col in ws.columns:
            max_length = 0
            col_letter = get_column_letter(col[0].column)
            
            for cell in col:
                try:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except:
                    pass
            
            ws.column_dimensions[col_letter].width = max(max_length + 2, 8)
        
        # Сохранение
        Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
        wb.save(xlsx_path)
        
    except csv.Error:
        raise ValueError("Ошибка формата CSV")
    except Exception as e:
        if isinstance(e, (FileNotFoundError, ValueError)):
            raise e
        raise ValueError(f"Ошибка конвертации: {e}")
```
![exe2!](/images/lab05/csv_xlsx.png) ![exe2!](/images/lab05/csv_xlsx1.png)
-------------------------------------------

