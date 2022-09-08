# Ejemplo para ver el error
num1 = 10
num2 = 0
# resultado = num1 / num2
# cambiamos num2 para evitar error
# num2 = 2
# Controlamos el error
try:
    num1 / num2
except:
    print("Ha ocurrido un error, no puedes dividir por 0")
# El else se ejecuta si no hay error
else:
    print("Esto se ejecuta si no hay error")
finally:
    print("Esto se ejecuta siempre")

# Generando una excepcion
num2 = 1
try:
    resultado = num1 / num2
    if num2 > 0:  # cambio para mostrar un error creado
        raise ValueError("Excepcion al dividir por cero")
except ValueError as ve:
    print(ve)
