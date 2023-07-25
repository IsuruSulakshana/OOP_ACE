#Parent class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print("name :",self.name)  #command 01
        print("age :",self.age)    #command 02
        
  
#Child class
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # call the __init__() method of the parent class
        self.employee_id = employee_id
        
    def display_info(self):
        super().display_info() #command 01, command 02
        print("employee id :",self.employee_id) #command 03
        
employee_A = Employee("John","24","EJ12345")
employee_A.display_info()