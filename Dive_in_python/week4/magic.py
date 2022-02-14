import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def __add__(self, other):
        obj = File(os.path.join(tempfile.gettempdir(), "tmp.txt"))
        obj.write(self.read() + other.read())
        return obj
    
    def __iter__(self):
        self.curr = 0
        with open(self.path, "r") as f:
            self.lines = f.readlines()
        return self
    
    def __next__(self):
        try:
            line = self.lines[self.curr]
            self.curr += 1
            return line
        except IndexError:
            raise StopIteration
    
    def __str__(self):
        return self.path
        
    def read(self):
        with open(self.path, "r") as f:
            return f.read()
        
    def write(self, data):
        with open(self.path, "w") as f:
            return f.write(data)