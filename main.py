class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def average_grade(self):
        average_grade = []  # Метод вычисления средней оценки за домашнее задание класса Student
        for curse_grade in self.grades.values():
            average_grade += curse_grade
        return round(sum(average_grade) / len(average_grade), 3)


    def __str__(self):  # Перегрузка вывода строки str класса Student
        res = (f'  Имя:  {self.name} \n  Фамилия:  {self.surname} \n  Средняя оценка за домашнее задание:'
               f'  {self.average_grade()} \n  Курсы в процессе обученияЖ:  {self.courses_in_progress}'
               f' \n  Завершённые курсы: {self.finished_courses} ')
        return res

    def __lt__(self,other): # Перегрузка сравнения студентов
        if not isinstance(other,Student):
            print('Not a student')
            return
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # Класс Лектор, наследуемый из класса Ментор с добавлением оценки лекций
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def average_grade(self):   # Вычисление средней оценки лекторов
        for average_grade in self.grades.values():
            pass
        return round(sum(average_grade) / len(average_grade),1)

    def __str__(self):  # Перегрузка метода str для класса Lecturer
        res = ( f'  Имя:  {self.name} \n  Фамилия:  {self.surname} \n  Средняя оценка за лекции:  '
                f'{self.average_grade()}')
        return res

    def __lt__(self,other):  # Перегрузка сравнения лекторов
        if not isinstance(other,Lecturer):
            print('Not a Lector')
            return
        return self.average_grade() > other.average_grade()


class Reviewer(Mentor):  # Класс проверятеля домашних заданий, наследуемый из класса Ментор


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):    # Перегрузка метода str для класса проверятелей домашних заданий
        res = f'  Имя:  {self.name} \n  Фамилия:  {self.surname} '
        return res

def average_home_work(list_student,course_name): # Функция вычисления средней оценки домашних заданий за курс
    list_grade = []
    for student in list_student:
        for course,grade in student.grades.items():
            if course_name == course:
                list_grade += grade
    return round(sum(list_grade)/len(list_grade),1)

def average_lecture_grade(list_lecture,course_name): # Функция вычисления средней оценки лекторов за курс
    list_grade = []
    for lecture in list_lecture:
        for course, grade in lecture.grades.items():
            if course_name == course:
                list_grade += grade
    return round(sum(list_grade) / len(list_grade), 1)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_copystudent = Student('CopyRuoy', 'CopyEman', 'your_gender')
best_copystudent.courses_in_progress += ['Python']
best_copystudent.courses_in_progress += ['Git']
best_copystudent.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_copystudent, 'Python', 9)
cool_reviewer.rate_hw(best_copystudent, 'Python', 8)
cool_reviewer.rate_hw(best_copystudent, 'Python', 7)

cool_copyreviewer = Reviewer('CopySome', 'CopyBuddy')
cool_copyreviewer.courses_attached += ['Git']

cool_copyreviewer.rate_hw(best_student, 'Git', 2)
cool_copyreviewer.rate_hw(best_student, 'Git', 2)
cool_copyreviewer.rate_hw(best_student, 'Git', 2)

cool_copyreviewer.rate_hw(best_copystudent, 'Git', 10)
cool_copyreviewer.rate_hw(best_copystudent, 'Git', 7)
cool_copyreviewer.rate_hw(best_copystudent, 'Git', 9)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 7)

cool_copylecturer = Lecturer('CopySome', 'CopyBuddy')
cool_copylecturer.courses_attached += ['Git']
best_student.rate_hw(cool_copylecturer, 'Git', 5)
best_student.rate_hw(cool_copylecturer, 'Git', 2)
best_student.rate_hw(cool_copylecturer, 'Git', 5)

print(cool_lecturer,'\n')
print(cool_copylecturer,'\n')

print(cool_reviewer,'\n')
print(cool_copyreviewer,'\n')

print(best_student,'\n')
print(best_copystudent, '\n')

print('Сравнение лекторов', cool_lecturer.__lt__(cool_copylecturer))
print('Сравнение студентов',best_student.__lt__(best_copystudent))

list_student = [best_student,best_copystudent]
specific_course = 'Python'
print(f'Средняя оценка за домашнее задание студентов курса {specific_course}:  {average_home_work(list_student,specific_course)}')

list_lecture = [cool_lecturer,cool_copylecturer]
print(f'Средняя оценка лекторов за {specific_course}: ',average_lecture_grade(list_lecture,specific_course))



