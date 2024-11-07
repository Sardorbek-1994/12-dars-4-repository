class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grades(self):
        return self.grades

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def add_grade(self, grade):
        self.grades.append(grade)
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

student = Student("Olim", 20, [85, 90, 78])
print(student.get_name())
print(student.get_age())
print(student.get_grades())

student.set_name("Anvar")
student.set_age(21)
student.add_grade(88)
print(student.get_name())
print(student.get_age())
print(student.get_grades())
print(student.average_grade())  
