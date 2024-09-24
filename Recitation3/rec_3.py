class Complex:
    def __init__(self, r, i):
        self._real = r
        self._imag = i

    def __str__(self):
        """Display Complex number"""
        if self._imag >= 0:
            # This is a string representation of the Complex object, not a Complex object
            return f"{self._real} + {self._imag}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__

    def conjugate(self):
        return Complex(self._real, -self._imag)

    def __rmul__(self,other):
        return self*other

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self._real*other._real - self._imag*other._imag
            imag_part = self._real*other._imag + self._imag*other._real
            ans = Complex(real_part, imag_part)
            return ans
        else:
            real_part = self._real*other
            imag_part = self._imag*other
            ans = Complex(real_part, imag_part)
            return ans