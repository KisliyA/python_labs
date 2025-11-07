# test_csv_xlsx.py
from csv_xlsx import csv_to_xlsx
import os

def test_csv_to_xlsx():
    """ CSV → XLSX """
    
    samples_dir = r'.\data\samples'
    print("=== Тест CSV → XLSX ===\n")
    
    # Тест 1: Корректный файл cities.csv
    print("1. cities.csv → cities.xlsx")
    try:
        csv_to_xlsx(f'{samples_dir}\\cities.csv', 'cities.xlsx')
        print("   ✓ Успешно")
    except Exception as e:
        print(f"   ✗ Ошибка: {e}")
    
    # Тест 2: Корректный файл people.csv
    print("\n2. people.csv → people.xlsx")
    try:
        csv_to_xlsx(f'{samples_dir}\\people.csv', 'people.xlsx')
        print("   ✓ Успешно")
    except Exception as e:
        print(f"   ✗ Ошибка: {e}")
    
    # Тест 3: Несуществующий файл
    print("\n3. Несуществующий файл")
    try:
        csv_to_xlsx(f'{samples_dir}\\nonexistent.csv', 'test.xlsx')
        print("   ✗ Ожидалась ошибка FileNotFoundError")
    except FileNotFoundError:
        print("   ✓ Корректно: FileNotFoundError")
    except Exception as e:
        print(f"   ✗ Неправильная ошибка: {e}")
    
    # Тест 4: Не CSV файл
    print("\n4. Файл с неправильным расширением")
    try:
        # Создаем текстовый файл
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write('name,age\nJohn,25')
        
        csv_to_xlsx('test.txt', 'test.xlsx')
        print("   ✗ Ожидалась ошибка ValueError")
    except ValueError:
        print("   ✓ Корректно: ValueError (неверный тип файла)")
    except Exception as e:
        print(f"   ✗ Неправильная ошибка: {e}")
    finally:
        # Удаляем временный файл
        if os.path.exists('test.txt'):
            os.remove('test.txt')
    
    # Тест 5: Пустой CSV файл
    print("\n5. Пустой CSV файл")
    try:
        # Создаем пустой CSV
        with open('empty.csv', 'w', encoding='utf-8') as f:
            f.write('')
        
        csv_to_xlsx('empty.csv', 'empty.xlsx')
        print("   ✗ Ожидалась ошибка ValueError")
    except ValueError:
        print("   ✓ Корректно: ValueError (пустой файл)")
    except Exception as e:
        print(f"   ✗ Неправильная ошибка: {e}")
    finally:
        # Удаляем временный файл
        if os.path.exists('empty.csv'):
            os.remove('empty.csv')

if __name__ == "__main__":
    test_csv_to_xlsx()
    print("\n✅ Все тесты завершены")