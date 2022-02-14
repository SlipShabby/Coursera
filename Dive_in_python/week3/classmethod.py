class Event:

    def __init(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

from datetime import date

event_description = date.today()

event = Event(event_description, event_date)
print(event)


def extract_description(user_string):
    return "football"

def extract_date(user_string):
    return date(2018, 6, 14)

class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_data

    def __str__(self):
         def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description
        date = extract_date(user_input)
        return cls(description, date)

# Staticmethod

class Human:

    def __init(sself, name, age = 0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

Human.is_age_valid(25)

human = Human("Old_Bobby")
human.is_age_valid(225)


# Property

class Robot:

    def __init__(self, power):
        self.power = power

wall_e = Robot(100)

wall_e.power = 200

# refactoring

class Robot:

    def __init__(self, power):
        self.power = power

    def set_power(self, power):
        if power < 0 :
            self.power = 0
        else:
            self.power = power

# use property


class Robot:

    def __init__(self, power):
        self.power = power


    power = property()

    @power.setter
    def power(self, value):
        if power < 0 :
            self._power = 0
        else:
            self._power = value

    @power_getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power


# alternative

class Robot:

    def __init__(self, power):
        self.power = power

    @property
    def power(self):
        # useful calculations
        return self._power
