from .models import Student
from .serialize import students_to_json, students_from_json
import os

def test_student():
    print(" Тест класса Student")
    student1 = Student(
        fio = "Иванов Иван Иванович",
        birthdate = "2007-06-15",
        group = "SE-01",
        gpa = 4.5
    )
    print("Студент создан")
    print(student1)
    print(f'Возраст: {student1.age()} лет')
    print(f'словарь:{student1.to_dict()}')
    print()

def test_serialization():
    print("Проверка сериализации")
    
    # Создаем папку, если она не существует
    os.makedirs("data/lab08", exist_ok=True)
    
    students = [
        Student("Иванов Иван Иванович", "2007-06-15", "SE-01", 4.5),
        Student("Петров Пётр Петрович", "2007-04-05", "SE-02", 3.8),
    ]
    
    # Сохраняем студентов
    students_to_json(students, "data/lab08/students_output.json")
    print("Студенты сохранены в students_output.json")

    # Проверяем, существует ли входной файлы
    input_file = "data/lab08/students_input.json"
    if os.path.exists(input_file):
        loaded_students = students_from_json(input_file)
        print("Студенты загружены из students_input.json")
        for student in loaded_students:
            print(f" - {student}")
    else:
        print(f"Входной файл {input_file} не найден. Создайте его.")
        # Создаем пример входного файла
        example_students = [
            Student("Киселев Александр", "2007-08-23", "SE-03", 4.5),
            Student("Артем Пойдашев", "2007-04-11", "SE-01", 4.0)
        ]
        students_to_json(example_students, input_file)
        print(f"Создан пример файла {input_file}")
    print()

def test_validation():
    print("Проверка валидации")
    try:
        Student('Тест', "2020-13-45", "SE-01", 3.0)
    except ValueError as e:
        print(f"Произошла ошибка валидации даты: {e} ")

    try:
        Student("Тест", "2020-01-01", "SE-02", 6)
    except ValueError as e:
        print(f"Произошла ошибка валидации GPA: {e} ")

if __name__ == "__main__":
    test_student()
    test_validation()
    test_serialization()