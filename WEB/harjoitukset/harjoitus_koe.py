class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def plot(self):
        print(f'My name is {self.first_name} {self.last_name}')

class Student(Person):
    def __init__(self, first_name, last_name, student_number):
        super().__init__(first_name, last_name)
        self.student_number = student_number

    def plot(self):
        super().plot()
        print(f'and my student number is {self.student_number}')


p1 = Person('James', 'Bond')
s1 = Student('Johnny', 'English', 321)

p1.plot()
s1.plot()