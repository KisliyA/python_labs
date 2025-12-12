from datetime import datetime, date
from dataclasses import dataclass

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # 1. Преобразуем GPA в float если это строка
        if isinstance(self.gpa, str):
            self.gpa = float(self.gpa)
        
        # 2. Валидация birthdate
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")

        # 3. Валидация GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне 0..5, получено: {self.gpa}")

    # Возраст студента
    def age(self) -> int:
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1
        return years
    
    # Сериализация
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    # Десериализация
    @classmethod
    def from_dict(cls, d: dict):
        # Преобразуем GPA при создании из словаря
        gpa = d["gpa"]
        if isinstance(gpa, str):
            gpa = float(gpa)
            
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=gpa
        )

    def __str__(self):
        return f"{self.fio} ({self.group}), возраст: {self.age()}, GPA: {self.gpa}"