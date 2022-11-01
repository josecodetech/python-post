paises = {'ESP','POR','ITA','FRA'}
print(paises)
print(type(paises))

#Los conjuntos no tienen datos repetidos
#Ver impresion
numeros = {1,2,2,2,3,4,5,8,1,0}
print(numeros)

#Creando desde cadena caracteres
#Observa que separa caracteres y solo incluye uno, no repite
cadena = set("Hacemos un conjunto desde esta frase")
print(cadena)
print(type(cadena))

#Podemos crear conjunto de diferentes tipos
tipos = {2,'Jose','josecodetech',True,23.43,'a'}
print(tipos)
print(type(tipos))