class Person:
    # Class attribute (static attribute)
    total_persons = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_persons += 1

    # Instance method
    def introduce(self):
        return f"Hi, my name is {self.name}, and I am {self.age} years old."

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Static method
    @staticmethod
    def count_persons():
        return Person.total_persons


# Usage of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 16)
person3 = Person("Charlie", 30)

# Using instance methods
print(person1.introduce())  
print(person2.introduce()) 
print(person3.introduce())  

# Using static methods
print(Person.is_adult(25))  
print(Person.is_adult(16))  


print(f"Total persons: {Person.count_persons()}")
