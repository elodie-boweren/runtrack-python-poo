class Person:
    def __init__(self):
        self.age = 14

    def display_age(self):
        print(self.age)
    
    def hello(self):
        print("Hello")

    def modify_age(self, new_age):
        self.age = new_age
    
class Student(Person):
    def __init__(self):
        Person.__init__(self)

    def go_to_class(self):
        print("I am going to class")

    def display_age(self):
        print(f"I am {self.age} years old")

class Professor(Person):
    def __init__(self, age):
        Person.__init__(self)
        self.__subject_taught = ""
        self.age = age

    def teach(self):
        print("The course will start")

#create a person
aida = Person()
aida.display_age()

#create a student
lucas = Student()
lucas.display_age()

lucas.hello()
lucas.go_to_class()
lucas.modify_age(15)
lucas.display_age()

#create a 40 yr old professor
morgan = Professor(40)
morgan.display_age()
morgan.hello()
morgan.teach()