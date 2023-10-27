class Triangulo:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return 'isósceles'
        return 'escaleno'
        