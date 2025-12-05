import json
from .models import Student
def students_to_json(students, path):
    "Сохранение списка студентов в JSON файл."
    data = [s.to_dict() for s in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def students_from_json(path) -> list[Student]:
    "Загрузка студентов из JSON файла."
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    result = []
    for d in raw:
        result.append(Student.from_dict(d))

    return result