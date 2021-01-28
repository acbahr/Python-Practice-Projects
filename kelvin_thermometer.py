class Thermometer:
    def __init__(self, kelvin):
        self.kelvin = kelvin    # default input is kelvin unless otherwise specified

    @property
    def fahrenheit(self):    # takes kelvin input and converts to fahrenheit
        return 32 + (9.0/5) * (self.kelvin - 273.15)

    @fahrenheit.setter
    def fahrenheit(self, value):    # takes fahrenheit input and converts to kelvin
        self.kelvin = 273.15 + (5.0/9) * (value - 32)    # changes self.kelvin member variable

    @property
    def celsius(self):    # takes kelvin input and returns celsius
        return self.kelvin - 273.15

    @celsius.setter
    def celsius(self, value):    # takes celsius input and returns kelvin
        self.kelvin = value + 273.15    # changes self.kelvin member variable


thermo = Thermometer(288.0)    # specifies kelvin input

print(round(thermo.kelvin, 2))    # returns kelvin
print(round(thermo.celsius, 2))    # returns celsius
thermo.fahrenheit = 68    # changes input to fahrenheit
print(round(thermo.kelvin, 2))    # returns kelvin from new fahrenheit input
print(round(thermo.celsius, 2))    # returns celsius from new fahrenheit input
