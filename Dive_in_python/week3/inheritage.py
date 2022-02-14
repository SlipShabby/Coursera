
class Pet:
    def __init__(self, name = None):
        self.name = name



class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}:waw".format(self.name)

dog = Dog("Lucky")
print(dog.name)
print(dog.say())



##

import json

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })


class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed = None):
        #call __mro__ 
        super().__init__(name, breed)
        # super(ExDog, self).__init__(name)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed = None):
        #clear pointing to the method
        super(Dog, self).__init__(name)
        self.breed = "woolen dog {0}".format(breed)

dog = WoolenDog("Grey", breed = "some")
print(dog.breed)


dog = ExDog("Belka", breed = "streetdog")
print(dog.to_json())


# object
#
# Pet       EportJSON
# Dog
#
#       ExDog

# Method resolution order
# ExDog.__mro__



# Private attr

class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return "{0}: waw!".format(self.name)

    def get_breed(self):
        return self.__breed
        
class ExportJSON:
    def to_json(self):
        pass

class ExDog(Dog, ExportJSON):
    def get_breed(self):
        return "breed type: {0} - {1}".format(self.name, self._Dog__breed)


dog = ExDog("Tuzik", "pittbull')
dog.get_breed()
# attr error

dog.__dict__
