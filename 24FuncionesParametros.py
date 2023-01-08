class Punto:
    def __init__(self,x=0,y=0):
        self.x = x 
        self.y = y
    def __repr__(self):
        return f"x: {self.x}\ny: {self.y}"
    
# creando objeto sin indicar los parametros
punto = Punto()
print(punto)
# indicando las coordenadas    
punto01 = Punto(1,2)
print(punto01)
# indicando una de las coordenadas    
punto02 = Punto(2)
print(punto02)
# indicando las coordenadas en otro orden    
punto03 = Punto(y=1,x=2)
print(punto03)
