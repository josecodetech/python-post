import random

# Condicional
num = int(input("Adivina el numero (1-3) : "))
numAzar = random.randint(1, 3)
if num == numAzar:
    print("Acertastes")
    print(f"El numero que pense era el {numAzar}")
elif num <= numAzar:
    print("El numero que indicas es menor")
else:
    print("El numero que indicas es mayor")
print("*"*25)
# Bucles
# Repeticion con for
# Saca numeros pares del intervalo 10 al 20 inclusive
for n in range(10, 21, 2):
    print(n)
print("*"*25)
# Recorre una cadena
texto = "Vamos a recorrer este texto caracter a caracter"
for caracter in texto:
    print(caracter)
print("*"*25)

# Repeticion while
suma = 0
contador = 0
while contador < 30:
    suma = suma + contador
    contador = contador+1
    if contador == 20:
        print(f"Saltamos el contador {contador}")
        continue
    if contador == 25:
        print(f"Salimos del bucle en contador {contador}")
        break
print(suma)
print("*"*25)

# modificacion adivina el numero mas completa con while
numAzar = random.randint(1, 20)
while True:
    num = int(input("Adivina el numero (1-20) : "))
    if num == numAzar:
        print("Acertastes")
        print(f"El numero que pense era el {numAzar}")
        break
    elif num <= numAzar:
        print("El numero que indicas es menor")
    else:
        print("El numero que indicas es mayor")
print("*"*25)
