# comprension de listas
# devolvemos una lista con los cuadrados
# de los numeros pares del 1 al 20 inclusives
lista = [x**2 for x in range(1, 21) if x % 2 == 0]
print(lista)

# funcion lambda
# anonima
lista2 = list(map(lambda x: x**2 if(x % 2 == 0) else 0, range(1, 21)))
print(lista2)
