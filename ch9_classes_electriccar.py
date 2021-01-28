# ---> inheritance: where a child class (ElectricCar) inherits all the attributes of the parent class (Car)
#      The child class can also add its own methods and attributes


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


class Battery():
    """A simple method to model a battery for an electric vehicle"""
    def __init__(self, battery_size=70):
        """Initialize the batteries attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def update_battery(self, new_battery_size):
        self.battery_size = new_battery_size

    def get_range(self):
        """Print a statement about the range this car has"""
        if self.battery_size == 70:
            range = 240
        if self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.\n'
        print(message)


class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        if model == 'model s':
            self.battery = Battery(85)  # calls the Battery instance (simplifies if classes get too long)
        elif model == 'model 3':
            self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2020)
my_tesla2 = ElectricCar('tesla', 'model 3', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print(my_tesla2.get_descriptive_name())
my_tesla2.update_odometer(50)
my_tesla2.read_odometer()
my_tesla2.battery.describe_battery()
my_tesla2.battery.get_range()
