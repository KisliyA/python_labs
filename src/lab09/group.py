import csv
from pathlib import Path
import sys

sys.path.append('/Users/alexk/dev/python_labs/src/lab08')
from models import Student

class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self):
        rows = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != self.HEADER:
                raise ValueError()
            for row in reader:
                Student(**row)  
                rows.append(row)
        return rows

    def _write_all(self, rows):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def is_empty(self):
        return len(self._read_all()) == 0

    def list(self):
        rows = self._read_all()
        return [Student(**r) for r in rows]

    def add(self, student):
        rows = self._read_all()
        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        })
        self._write_all(rows)

    def find(self, substr):
        substr = substr.lower()
        rows = self._read_all()
        return [Student(**r) for r in rows if substr in r["fio"].lower()]

    def remove(self, fio):
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        self._write_all(new_rows)

    def update(self, fio, **fields):
        rows = self._read_all()
        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    if k in self.HEADER:
                        r[k] = v
                Student(**r)  
        self._write_all(rows)

    def stats(self):
        rows = self._read_all()
        if not rows:
            return {"count": 0, "average_gpa": 0, "top_5_students": []}
        gpas = [float(r["gpa"]) for r in rows]
        sorted_rows = sorted(rows, key=lambda x: float(x["gpa"]), reverse=True)
        return {
            "count": len(rows),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "top_5_students": sorted_rows[:5]
        }

if __name__ == "__main__":
    import os
    
    # Переход в корень проекта
    project_root = "/Users/alexk/dev/python_labs"
    os.chdir(project_root)
    
    # Путь
    csv_path = "data/lab09/students.csv"
    
    # Создаем папку
    os.makedirs("data/lab09", exist_ok=True)
    
    # Удаляем старый файл
    if os.path.exists(csv_path):
        os.remove(csv_path)
    
    group = Group(csv_path)
    
    print("Тест методов Group:")
    print("-" * 25)
    
    # 1. add()
    group.add(Student("Иванов Иван", "2000-01-01", "Группа-1", 4.5))
    group.add(Student("Петров Петр", "2001-02-02", "Группа-2", 3.8))
    
    # 2. list()
    print("\nlist():")
    for s in group.list():
        print(f"  {s}")
    
    # 3. find()
    print("\nfind('Иванов'):")
    for s in group.find("Иванов"):
        print(f"  {s}")
    
    # 4. update()
    print("\nupdate('Иванов Иван', gpa=5.0):")
    group.update("Иванов Иван", gpa=5.0)
    print(f"  Результат: {group.find('Иванов')[0]}")
    
    # 5. remove()
    print("\nremove('Петров Петр'):")
    group.remove("Петров Петр")
    print(f"  Осталось: {len(group.list())} студент(ов)")
    
    print(f"\n Файл: {csv_path}")