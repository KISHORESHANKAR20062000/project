class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self, age):
        return self.age

    def get_grade(self, grade):
        return self.grade


class course:
    def __init__(self, subname, max_student):
        self.subname = subname
        self.max_student = max_student
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            print(" added to")
            return True
        else:
            print("Course full")

    def calculate_average(self):
        value = 0
        for value in self.students:
            value += self.get_grade()
        return value / len(self.students)


s1 = student("kishore", 20, 50)
s2 = student("guru", 20, 20)
s3 = student("karthi", 20, 75)
s6 = student("vignesh", 28, 75)
s5 = student("bala", 26, 75)
s4 = student("ARUN", 27, 95)
s7 = student("branch", 23, 95)
s8 = student("new branch", 23, 95)
Course = course('science', 2)
Course.add_students(s1)
Course.add_students(s2)
print(course.calculate_average())