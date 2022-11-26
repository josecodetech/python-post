# Funcion calcula media - normal
def media(numeros):
    suma = 0
    cantidad = 0
    for numero in numeros:
        suma = suma + int(numero)
        cantidad = cantidad + 1
    media = suma / cantidad
    return media
# Llamada a funcion
numeros = [1,23,54,83,12,54,55,65,21,2,9]
print(media(numeros))

# Opcion con list Comprehension
x=[int(x) for x in numeros]
print(sum(x)/len(x))