import random

#5 numeros entre 0 y 1
for i in range(5):
    print(random.random())
    
#5 numeros decimales entre intervalos dados
for i in range(5):
    print(random.uniform(10,21))

#5 numeros enteros entre intervalo dado
for i in range(5):
    print(random.randint(15,51))

#Seleccionar al azar de lista
colores = ('rojo','verde','azul','amarillo')
print(random.choices(colores,k=1))        