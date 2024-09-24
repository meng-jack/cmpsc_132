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

    def __rmul__(self, other):
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


class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)

    def __eq__(self, other):
        ''' Returns True if other is a Real object that has the same value or if other is
            a Complex object with _imag=0 and same value for _real, False otherwise

            >>> Real(4) == Real(4)
            True
            >>> Real(4) == Real(4.0)
            True
            >>> Real(5) == Complex(5, 0)
            True
            >>> Real(5) == Complex(5, 12)
            False
            >>> Real(5) == 5.5
            False
        '''
        return other._imag == self._imag and other._real == self._real if isinstance(other, Complex) else self._real == other

    def __int__(self):
        return int(self._real)

    def __float__(self):
        return float(self._real)
