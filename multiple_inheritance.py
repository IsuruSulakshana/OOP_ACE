class Father:
    def __init__(self,father_name):
        self.father_name = father_name
        
    def display_father(self):
        print("Father name :",self.father_name)
    
class Mother:
    def __init__(self,mother_name):
        self.mother_name = mother_name
        
    def display_mother(self):
        print("Mother name :",self.mother_name)

class Child(Father,Mother):
    def __init__(self, child_name, father_name, mother_name):
        super().__init__(father_name)
        Mother.__init__(self,mother_name)
        self.child_name = child_name
        
    def display_child(self):
        print("Child name :",self.child_name)
        
        
child_A = Child("Tom","John","Emily")

child_A.display_child()
child_A.display_father()
child_A.display_mother()