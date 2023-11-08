class Rational:
    def __init__(self, a1, a2):
        c = self.gcd(a1, a2)
        self.a = int(a1/c)
        self.b = int(a2/c)
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b
    def gcd(self, a, b):
        A = abs(a)
        B = abs(b)
        if A < B:
            A, B = B, A

        while A % B != 0:
            A, B = B, (A % B)
        return B
    
    def __str__(self):
        return str(self.a) + '/' + str(self.b)
    
    def __add__(self, x):
        z = self.gcd(self.b, x.b)
        e = self.b / z
        f = x.b / z
        return Rational(self.a * f + x.a * e, x.b * e)
    
    def __sub__(self, x):
        z = self.gcd(self.b, x.b)
        e = self.b / z
        f = x.b / z
        return Rational(self.a * f - x.a * e, x.b * e)
    
    def __mul__(self, x):
        return Rational(self.a * x.a, self.b * x.b)
    
    def __truediv__(self, x):
        return Rational(self.a * x.b, self.b * x.a)
    
    def __float__(self):
        return float(self.a/self.b)