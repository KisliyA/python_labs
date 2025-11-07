from pathlib import Path
import json, csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Функция конвертирует JSON-файл в CSV-файл'''
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
    '''Функция конвертирует CSV-файл в JSON-файл'''
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