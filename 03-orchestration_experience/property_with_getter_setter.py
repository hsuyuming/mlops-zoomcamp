class Celsius:

    def __init__(self, temperature=0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting Value...")
        return self._temperature
    
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value
    
    # property(fget=None, fset=None, fdel=None, doc=None)
    temperature = property(get_temperature, set_temperature)

human = Celsius(37)
print(human.temperature)
print(human._temperature)
print(human.to_fahrenheit())
human.temperature = -300