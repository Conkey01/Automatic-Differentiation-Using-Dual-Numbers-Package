import math

class Dual:
    def __init__(self, real, dual=0):
        """
        Represents a dual number: real + dual * ε
        :param real: The real part of the dual number
        :param dual: The dual part of the dual number
        """
        self.real = real
        self.dual = dual

    def __repr__(self):
        return f"Dual(real={self.real}, dual={self.dual})"

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        return Dual(self.real + other, self.dual)

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        return Dual(self.real - other, self.dual)

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(
                self.real * other.real,
                self.real * other.dual + self.dual * other.real,
            )
        return Dual(self.real * other, self.dual * other)

    def __truediv__(self, other):
        if isinstance(other, Dual):
            real = self.real / other.real
            dual = (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            return Dual(real, dual)
        return Dual(self.real / other, self.dual / other)

    def sin(self):
        return Dual(math.sin(self.real), self.dual * math.cos(self.real))

    def cos(self):
        return Dual(math.cos(self.real), -self.dual * math.sin(self.real))

    def tan(self):
        return Dual(math.tan(self.real), self.dual / (math.cos(self.real) ** 2))

    def log(self):
        return Dual(math.log(self.real), self.dual / self.real)

    def exp(self):
        exp_real = math.exp(self.real)
        return Dual(exp_real, self.dual * exp_real)
