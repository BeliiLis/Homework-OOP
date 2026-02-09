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

    def _average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0.0

    def __str__(self):
        avg_grade = self._average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses = ", ".join(self.finished_courses) if self.finished_courses else "Нет"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() == other._average_grade()


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

    def _average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0.0

    def __str__(self):
        avg_grade = self._average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() == other._average_grade()


class Reviewer(Mentor):
    """Класс проверяющих (наследуется от Mentor)"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
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

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАНИЯ №3: Магические методы и сравнения")
    print("=" * 60)
    
    student = Student('Ruoy', 'Eman', 'М')
    student.courses_in_progress = ['Python', 'Git']
    student.finished_courses = ['Введение в программирование']
    student.grades = {'Python': [10, 9, 10], 'Git': [9, 8]}
    
    lecturer = Lecturer('Some', 'Buddy')
    lecturer.courses_attached = ['Python']
    lecturer.grades = {'Python': [9, 10, 9, 10]}
    
    reviewer = Reviewer('Some', 'Buddy')
    reviewer.courses_attached = ['Python', 'Git']
    
    print("\n--- Вывод информации о проверяющем (Reviewer) ---")
    print(reviewer)
    
    print("\n--- Вывод информации о лекторе (Lecturer) ---")
    print(lecturer)
    
    print("\n--- Вывод информации о студенте (Student) ---")
    print(student)
    
    print("\n--- Сравнение студентов ---")
    student2 = Student('John', 'Doe', 'М')
    student2.grades = {'Python': [8, 7, 9]}
    print(f"Студент 1 (средняя: {student._average_grade()}): {student.name} {student.surname}")
    print(f"Студент 2 (средняя: {student2._average_grade()}): {student2.name} {student2.surname}")
    print(f"Студент 1 > Студент 2: {student > student2}")
    print(f"Студент 1 == Студент 2: {student == student2}")
    
    print("\n--- Сравнение лекторов ---")
    lecturer2 = Lecturer('Best', 'Lecturer')
    lecturer2.grades = {'Python': [10, 10, 10]}
    print(f"Лектор 1 (средняя: {lecturer._average_grade()}): {lecturer.name} {lecturer.surname}")
    print(f"Лектор 2 (средняя: {lecturer2._average_grade()}): {lecturer2.name} {lecturer2.surname}")
    print(f"Лектор 1 < Лектор 2: {lecturer < lecturer2}")