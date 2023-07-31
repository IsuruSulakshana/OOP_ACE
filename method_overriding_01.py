class Person:
    def greet(self):
        return "Hello I'm a Person"
    
class Student(Person):
    def greet(self):
        return "Hello I'm a Student"
    
Person = Person()
Student = Student()

print(Person.greet())
print(Student.greet())