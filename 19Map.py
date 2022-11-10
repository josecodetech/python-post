numeros = [1,2,3,4,6,8,3,2,9]
resultado = []
# Mediante bucle
for i in numeros:
    resultado.append(i**2)
print(numeros)
print(resultado)

# Con map, devuelve lista
# usando funcion lambda
resultado02=list(map(lambda i: i**2,numeros))
print(resultado02)

# Otro ejemplo
resultado03=list(map(lambda x, y: x+y,numeros,resultado02))
print(resultado03)