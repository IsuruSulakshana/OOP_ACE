class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_text(self, number, message):
        print(f"Sending text to {number}: {message}")


class Smartphone(Phone):
    def __init__(self, brand, model, operating_system):
        super().__init__(brand, model)
        self.operating_system = operating_system

    def install_app(self, app_name):
        print(f"Installing {app_name} from the app store.")


class BasicPhone(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)


# Usage of the Phone, Smartphone, and BasicPhone classes
phone = Phone("Nokia", "3310")
phone.make_call("123456789")
phone.send_text("123456789", "Hello!")

print("\n")

smartphone = Smartphone("Apple", "iPhone 13", "iOS")
smartphone.make_call("987654321")
smartphone.send_text("987654321", "Hi there!")
smartphone.install_app("Instagram")

print("\n")

basic_phone = BasicPhone("Samsung", "Guru")
basic_phone.make_call("555555555")
basic_phone.send_text("555555555", "Goodbye!")
