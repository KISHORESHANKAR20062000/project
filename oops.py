class person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
class manager(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def manager_salary(self):
        print(f"{self.name} is a manager {self.salary*1.3}is his salary ")

class programmer(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
    def programmer_salary(self):
        print(f"{self.name} is a programmer {self.salary*1.5}is his salary")

p1 = manager("kishore", 20, 3000)
p2 = programmer("karthi", 20, 4000)
p2.programmer_salary()
print(f"{p2.get_salary()} is his basic pay")