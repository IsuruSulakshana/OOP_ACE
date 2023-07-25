class Phone:
    
    def say(self,name):
        print("Hello", name)
        

phone_A = Phone()
phone_A.say("Nokia")
print(phone_A.name)
phone_A.name = "Samsung"
print(phone_A.name)

phone_B = Phone()
phone_B.say("Apple")