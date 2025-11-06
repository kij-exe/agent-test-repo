import math

class Vector:
    def __init__(self, *args):
        self.values = args

    def __add__(self, other):
        return Vector(*(a+b for a, b in zip(self.values, other.values)))

    def __sub__(self, other):
        return Vector(*(a-b for a, b in zip(self.values, other.values)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(*(a*b for a, b in zip(self.values, other.values)))
        else:
            return Vector(*(a*other for a in self.values))

    def dot(self, other):
        return sum(a*b for a, b in zip(self.values, other.values))

    def __repr__(self):
        return f'Vector({', '.join(map(str, self.values))})'
