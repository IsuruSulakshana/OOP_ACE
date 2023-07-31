class person:
    def __init__(self, name, age):
        #print("Hello!")
        self.name = name
        self.age = age
        
    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old")

#creating objects of the person class
person1 = person("John", 22)
person2 = person("Tom", 24)

#calling the introduce method on the objects
person1.introduce()
# person2.introduce()

# print(person1.name)
person1.name = "Bob"
person1.age = 27
person1.introduce()
