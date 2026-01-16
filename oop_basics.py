class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old and I study {self.course}.")


student1 = Student("Agni", 19, "Computer Science")
student1.introduce()
