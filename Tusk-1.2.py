# Задание №1: Наследование

class Student:
    """Класс студентов"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    """Родительский класс для преподавателей"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лекторов (наследуется от Mentor)"""
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Reviewer(Mentor):
    """Класс проверяющих (наследуется от Mentor)"""
    def __init__(self, name, surname):
        super().__init__(name, surname)


# Тестирование задания №1
if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАНИЯ №1: Наследование")
    print("=" * 60)
    
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    
    print(f"isinstance(lecturer, Mentor): {isinstance(lecturer, Mentor)}")  # True
    print(f"isinstance(reviewer, Mentor): {isinstance(reviewer, Mentor)}")  # True
    print(f"lecturer.courses_attached: {lecturer.courses_attached}")  # []
    print(f"reviewer.courses_attached: {reviewer.courses_attached}")  # []