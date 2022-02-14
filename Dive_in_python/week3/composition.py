import json



class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None):
        super().__init__(name)
        self.breed = breed

class ExDog(Dog):
    def __init__(self, name, breed = None, exporter= None):
        super().__init__(name, breed = None)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad exporter", export)

    def exporter(self):
            return self._exporter.export(self)

# class ExportJSON(Pet):
#     pass

# class ExDog(Dog, ExportJSON):
#     pass

# class ExportJSON:
#     def to_json(self):
#         pass

# class ExportXML():
#     def to_xml(self):
#         pass

# class ExDog(Dog, ExportJSON, ExportXML):
#     pass

# dog = ExDog("Lucky", "terrier", exporter=ExportXML())
# dog.export()

class PetExport:
    def export(self, Dog):
        raise NotImplementedError

class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name
            "breed": dog.breed
        })


class ExportXML(PetExport):
    def export(self, dog):
        return """<?xml version="1.0"encoding="utf-8"?>

<dog>
<name>{0}</name>
<breed>{1}</breed>
</dog>
""".format(dog.name, dog.breed)


dog = ExDog("Lucky", "terrier", exporter=ExportXML())
dog.export()

