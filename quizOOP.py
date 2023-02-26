class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, mentor, course, grade):
        if isinstance(mentor, Mentor) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in Lecturer.grades:
                Lecturer.grades[course] += [grade]
            else:
                Lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        av_rating = round(sum_rating / len_rating, 2)
        return av_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_rating()}\n' \
              f' Курсы в процессе обучения: {self.courses_in_progress}\n завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def average_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        av_rating = round(sum_rating / len_rating, 2)
        return av_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподавателей и студентов между собой не сравнивают!")
            return
        return self.average_rating() < other.average_rating()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res


# Студенты
student_1 = Student('Александр', 'Антонов', 'Муж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в программирование", "Git"]

student_2 = Student('Валерия', 'Солнцева', 'Жен')
student_2.courses_in_progress += ['Python', 'PostgreSQL']
student_2.finished_courses += ["Введение в программирование"]

# Лекторы
lecturer_1 = Lecturer('Сергей', 'Василевский')
lecturer_1.courses_attached += ['Python', 'Git', 'Java']

lecturer_2 = Lecturer('Марина', 'Димитрова')
lecturer_2.courses_attached += ['Python', 'Git', 'JavaScript', 'PostgreSQL']

# Проверяющие
reviewer_1 = Reviewer('Алина', 'Мезенцева')
reviewer_1.courses_attached += ['Python', 'PostgreSQL', 'Java']

reviewer_2 = Reviewer('Алексей', 'Малютин')
reviewer_2.courses_attached += ['Python', 'Git', 'JavaScript']

# Оценки по студентам
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'PostgreSQL', 10)

# Списки по принадлежности
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


def average_rating_for_course(course, student_list):
    summary_rating = 0
    quantity_rating = 0
    for student in student_list:
        for course in student.grades:
            student_summary_rating = student.av_rating_for_course(course)
            summary_rating += student_summary_rating
            quantity_rating += 1
    average_rating = round(summary_rating / quantity_rating, 2)
    return average_rating


# print
print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
