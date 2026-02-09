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


def average_grade_students(students, course):
    all_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            all_grades.extend(student.grades[course])
    
    if not all_grades:
        return f"Нет оценок по курсу '{course}'"
    return round(sum(all_grades) / len(all_grades), 1)


def average_grade_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    
    if not all_grades:
        return f"Нет оценок по курсу '{course}'"
    return round(sum(all_grades) / len(all_grades), 1)


if __name__ == "__main__":
    print("=" * 70)
    print("ПОЛЕВЫЕ ИСПЫТАНИЯ — ЗАДАНИЕ №4")
    print("=" * 70)
    
    student1 = Student('Алиса', 'Селезнева', 'Ж')
    student1.courses_in_progress = ['Python', 'Java']
    student1.finished_courses = ['Основы программирования']
    student1.grades = {'Python': [8, 9, 7], 'Java': [10, 9]}
    
    student2 = Student('Вася', 'Пупкин', 'М')
    student2.courses_in_progress = ['Python', 'C++']
    student2.finished_courses = ['Алгоритмы']
    student2.grades = {'Python': [7, 8, 8], 'C++': [9, 10]}
    
    lecturer1 = Lecturer('Иван', 'Петров')
    lecturer1.courses_attached = ['Python', 'Java']
    lecturer1.grades = {'Python': [9, 8, 10], 'Java': [7, 8]}
    
    lecturer2 = Lecturer('Мария', 'Сидорова')
    lecturer2.courses_attached = ['Python', 'C++']
    lecturer2.grades = {'Python': [10, 9, 9], 'C++': [8, 9]}
    
    reviewer1 = Reviewer('Алексей', 'Смирнов')
    reviewer1.courses_attached = ['Python', 'Java']
    
    reviewer2 = Reviewer('Елена', 'Козлова')
    reviewer2.courses_attached = ['Python', 'C++']
    
    print("\n1. Выставление оценок студентам рецензентами:")
    print(f"  reviewer1.rate_hw(student1, 'Python', 9): {reviewer1.rate_hw(student1, 'Python', 9)}")
    print(f"  reviewer2.rate_hw(student2, 'C++', 10): {reviewer2.rate_hw(student2, 'C++', 10)}")
    print(f"  reviewer1.rate_hw(student2, 'Java', 8): {reviewer1.rate_hw(student2, 'Java', 8)}")
    
    print("\n2. Выставление оценок лекторам студентами:")
    print(f"  student1.rate_lecture(lecturer1, 'Python', 10): {student1.rate_lecture(lecturer1, 'Python', 10)}")
    print(f"  student2.rate_lecture(lecturer2, 'C++', 9): {student2.rate_lecture(lecturer2, 'C++', 9)}")
    print(f"  student1.rate_lecture(lecturer2, 'Java', 8): {student1.rate_lecture(lecturer2, 'Java', 8)}")
    
    print("\n3. Вывод информации через магический метод __str__:")
    print("\n--- Студент 1 ---")
    print(student1)
    print("\n--- Студент 2 ---")
    print(student2)
    print("\n--- Лектор 1 ---")
    print(lecturer1)
    print("\n--- Лектор 2 ---")
    print(lecturer2)
    print("\n--- Рецензент 1 ---")
    print(reviewer1)
    print("\n--- Рецензент 2 ---")
    print(reviewer2)
    
    print("\n4. Сравнение объектов:")
    print(f"  Студент 1 < Студент 2: {student1 < student2}")
    print(f"  Студент 1 == Студент 2: {student1 == student2}")
    print(f"  Лектор 1 < Лектор 2: {lecturer1 < lecturer2}")
    print(f"  Лектор 1 == Лектор 2: {lecturer1 == lecturer2}")
    
    print("\n5. Расчет средних оценок по курсам:")
    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]
    
    avg_python_students = average_grade_students(students_list, 'Python')
    print(f"  Средняя оценка студентов по курсу 'Python': {avg_python_students}")
    
    avg_python_lecturers = average_grade_lecturers(lecturers_list, 'Python')
    print(f"  Средняя оценка лекторов по курсу 'Python': {avg_python_lecturers}")
    
    avg_java_students = average_grade_students(students_list, 'Java')
    print(f"  Средняя оценка студентов по курсу 'Java': {avg_java_students}")
    
    avg_cpp_lecturers = average_grade_lecturers(lecturers_list, 'C++')
    print(f"  Средняя оценка лекторов по курсу 'C++': {avg_cpp_lecturers}")