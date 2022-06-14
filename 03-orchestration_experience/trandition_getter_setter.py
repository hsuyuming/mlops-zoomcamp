class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32


    def get_temperature(self):
        return self._temperature
    
    
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

human = Celsius(37)

print(human.get_temperature())

print(human.to_fahrenheit())

human.set_temperature(-300)
# Traceback (most recent call last):
#   File "/test.py", line 24, in <module>
#     human.set_temperature(-300)
#   File "/test.py", line 15, in set_temperature
#     raise ValueError("Temperature below -273.15 is not possible.")
# ValueError: Temperature below -273.15 is not possible.
print(human.to_fahrenheit())