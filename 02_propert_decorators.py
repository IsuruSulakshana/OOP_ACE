class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be less than -273.15 degrees Celsius.")
        self._temperature = value

    @property
    def fahrenheit(self):
        return self._temperature * 9/5 + 32

temp = Celsius(25)
print(temp.temperature)  # Output: 25
print(temp.fahrenheit)  # Output: 77.0

temp.temperature = 30
print(temp.temperature)  # Output: 30
print(temp.fahrenheit)  # Output: 86.0

temp.temperature = -300  # Raises ValueError: Temperature cannot be less than -273.15 degrees Celsius.
