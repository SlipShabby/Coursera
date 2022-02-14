
class Human:
    pass

class Robot:
    ''' definition'''

class Planet:
    pass

planet = Planet()

solar_system = []
for i in range(8):
    planet = Planet()
    solar_system[planet] = True

class Planet:

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"Planet {self.name}"    


earth = Planet("Earth")


solar_system = []
planets = [''Moon, 'Mars', 'Jupiter']

for name in planets:
    planet = Planet(name)
    solar_system.append(planet)


class Planet:

    count = 0

    def __init__(self, name, population = None):
        self.name = name
        self.population = population or []
        Planet.count += 1

    earth = Planet("Earth")
    mars = Planet("Mars")

    print(Planet.count)

    class Human:
        def __del__(self):
            print('Goodbye!')



    class Planet:

        count = 1

        def __init__(self, name, population = None):
            self.name = name
            self.population = population or []

    planet = Planet("Earth")

    planet.__dict__

    planet.mass = 5.4

    planet.__dict__

    Planet.__dict__


class Planet:

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super(): __new__(cls)
        return obj

        def __init__(self, name):
            print("__init__ called")
            self.name = name


planet = Planet.__new__(Planet, "Earth")

if isinstance(planet, Planet):
    Planet.__init__(planet, "Earth")





    



