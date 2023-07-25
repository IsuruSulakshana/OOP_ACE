class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age

person_A = person("john",20) 

print(person_A.name)
print(person_A.get_age())
person_A.set_age(28)
print(person_A.get_age())