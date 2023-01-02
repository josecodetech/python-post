lista = [1,2,3,4,5,6,7,8,9,10]
# Forma normal
cuadrado = []
for item in lista:
    cuadrado.append(item**2)
print(lista)
print(cuadrado)

# List comprenhension
cuadrado = [i**2 for i in lista]
print(lista)
print(cuadrado)