# Obtener datos del usuario
# y guardarlos en variable
# strip elimina los espacios
nombre = input("Dime tu nombre : ").strip()
# por omision se obtiene un string
# para cambiarlo en este caso usamos int
numero = int(input("Dime un numero : "))

# Mostramos por consola los valores obtenidos
print(f"Tu nombre es {nombre}")
print(f"Y el numero que me has indicado es {numero}")