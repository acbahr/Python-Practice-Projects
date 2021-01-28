"""
Add a TKinter GUI to this thermometer program
"""

class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return round(32 + (9/5) * self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = round((value - 32) / (9/5))


thermo = Thermometer(15)
print(thermo.fahrenheit)
thermo.fahrenheit = 68
print(thermo.celsius)


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return self.first + " " + self.last

    @full_name.setter
    def full_name(self, new_name):
        first, last = new_name.split()
        self.first = first
        self.last = last

guy = Person("John", "Doe")
print(guy.full_name)

guy.full_name = "Aaron Bahr"
print(guy.full_name)



