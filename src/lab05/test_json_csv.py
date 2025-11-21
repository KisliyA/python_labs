# absolute_test.py
from json_csv import json_to_csv, csv_to_json
import os

samples_dir = r'.\data\samples'

print("=== Тест ===")

# Тест 1: cities.csv
try:
    path = os.path.abspath(os.path.join(samples_dir, 'cities.csv'))
    csv_to_json(
        path, 
        'cities_output.json'
    )
    print("✓ cities.csv → cities_output.json: Успешно")
except Exception as e:
    print(f"✗ cities.csv: {e}")

# Тест 2: people.csv  
try:
    path = os.path.abspath(os.path.join(samples_dir, 'people.csv'))
    csv_to_json(
        path,
        'people_output.json'
    )
    print("✓ people.csv → people_output.json: Успешно")
except Exception as e:
    print(f"✗ people.csv: {e}")

# Тест 3: people.json
try:
    path = os.path.abspath(os.path.join(samples_dir, 'people.json'))
    json_to_csv(
        path,
        'people_output.csv'
    )
    print("✓ people.json → people_output.csv: Успешно")
except Exception as e:
    print(f"✗ people.json: {e}")

print("\n=== Тесты завершены ===")