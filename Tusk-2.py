class Student:
    """Класс студентов"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """
        Выставление оценки лектору за лекцию.
        """
        if not isinstance(lecturer, Lecturer):
            return "Ошибка: оценку можно выставлять только лектору"
        if course not in self.courses_in_progress:
            return f"Ошибка: студент {self.name} {self.surname} не обучается на курсе '{course}'"
        if course not in lecturer.courses_attached:
            return f"Ошибка: лектор {lecturer.name} {lecturer.surname} не ведет курс '{course}'"
        if not isinstance(grade, int) or grade < 1 or grade > 10:
            return "Ошибка: оценка должна быть целым числом от 1 до 10"
        
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return None


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
        self.grades = {}


class Reviewer(Mentor):
    """Класс проверяющих (наследуется от Mentor)"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Выставление оценки студенту за домашнее задание.
        """
        if not isinstance(student, Student):
            return "Ошибка: оценку можно выставлять только студенту"
        if course not in self.courses_attached:
            return f"Ошибка: проверяющий {self.name} {self.surname} не прикреплен к курсу '{course}'"
        if course not in student.courses_in_progress:
            return f"Ошибка: студент {student.name} {student.surname} не обучается на курсе '{course}'"
        if not isinstance(grade, int) or grade < 1 or grade > 10:
            return "Ошибка: оценка должна быть целым числом от 1 до 10"
        
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАНИЯ №2: Методы выставления оценок")
    print("=" * 60)
    
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    student = Student('Ольга', 'Алёхина', 'Ж')
    
    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']
    
    print("Тест 1: Корректная оценка лектору")
    result = student.rate_lecture(lecturer, 'Python', 7)
    print(f"  student.rate_lecture(lecturer, 'Python', 7): {result}") 
    
    print("\nТест 2: Студент не учится на курсе у лектора")
    result = student.rate_lecture(lecturer, 'Java', 8)
    print(f"  student.rate_lecture(lecturer, 'Java', 8): {result}") 
    
    print("\nТест 3: Опечатка в названии курса")
    result = student.rate_lecture(lecturer, 'С++', 8)
    print(f"  student.rate_lecture(lecturer, 'С++', 8): {result}") 
    
    print("\nТест 4: Попытка оценить рецензента")
    result = student.rate_lecture(reviewer, 'Python', 6)
    print(f"  student.rate_lecture(reviewer, 'Python', 6): {result}") 
    
    print(f"\nИтоговые оценки лектора: {lecturer.grades}")  