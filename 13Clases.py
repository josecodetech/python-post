class Figura:
    """Figura geometrica con base y altura"""
    # Constructor

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return(
            f"Soy una figura de {self.base} de base y {self.altura} de altura")


class Rectangulo(Figura):
    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def area(self):
        return (self.base * self.altura)/2


mi_figura = Figura(10, 15)
print(mi_figura)
rectangulo = Rectangulo(10, 20)
triangulo = Triangulo(20, 10)
print("El area del rectangulo es ", rectangulo.area())
print("El area del triangulo es ", triangulo.area())
