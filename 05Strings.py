# asignacion a variables
cadena1 = "Hola, "
cadena2 = "Mundo!"
# concatenar cadenas
print(cadena1+cadena2)
# mostrar caracter por posicion (empieza por el 0)
print(cadena1[2])
# por un intervalo
print(cadena1[2:5])
# eliminando espacio o caracter indicado
print(cadena1.split('l'))
print(cadena1.split(' '))
lista_caracteres = ['h', 'o', 'l', 'a']
print(lista_caracteres)
# union
cadena_nueva = ''.join(lista_caracteres)
print(cadena_nueva)
# convierte a mayusculas
print(cadena1.upper())
# convierte a minusculas
print(cadena1.lower())
# en mayusculas la primera letra
print(cadena1.capitalize())
# longitud cadena
print(len(cadena1))
# Conversion a cadena
print(type(str(234)))
# Mostrar variables dentro de una cadena
# La \con " es para mostrar las comillas con el escape
print(f"Texto mostrando variable \"cadena\" {cadena1}")
