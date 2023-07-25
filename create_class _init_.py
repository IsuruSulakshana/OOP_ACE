class Phone:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("Hello" , self.name)
        

phone_A = Phone("Nokia")
phone_A.say()
phone_A.name = "Apple"
phone_A.say()

phone_B = Phone("Samsung")
phone_B.say()
print(phone_B.name)
