class Human:
    def __init__(self, name, age = 0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self.say(f"Hello, I am {self._name}")

    
    bob = Human("Bob", age = 29)

    bob.say_name()
    
    print(bob._name)

    bob._say("something")

    