# car.py
# --> working with classes and instances

"""
---> Once you write a class, you'll spend most of your time working with instances created from that class.
One of the first tasks you'll want to do is modify the attributes associated with a particular instance.
You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

---> Let's write a new class representing a car. Our class will store information about the
kind of car we're working with, and it will have a method that summarizes this information:
"""


class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing a cars mileage"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value
        Reject the change if it tries to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back the odometer!")


my_new_car = Car('toyota', 'tundra', '2021')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# You can change an attribute's value (odometer reading in this case) in three ways: you can change the value
# directly through an instance, set the value through a method, or increment the value
# (add a certain amount to it) through a method

# directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# modify through a method
my_new_car.update_odometer(21)
my_new_car.read_odometer()

# incrementing attribute value through a method
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# second car
my_old_car = Car('toyota', 'corolla', 2010)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(46000)
my_old_car.read_odometer()
my_old_car.increment_odometer(-3000)
my_old_car.read_odometer()
