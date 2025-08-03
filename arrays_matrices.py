# arrays_matrices.py
class Array:
    def __init__(self):
        self.data = []
    def insert(self, value):
        self.data.append(value)
    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
    def access(self, index):
        return self.data[index] if 0 <= index < len(self.data) else None
