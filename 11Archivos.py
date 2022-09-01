# Archivos
# Escritura
archivo = open('fichero.txt', 'w')
archivo.write("Estoy escribiendo en fichero\n")
archivo.write("Escribo segunda linea")
archivo.close()
# Lectura
archivo = open('fichero.txt', 'r')
lineas = archivo.readlines()
for linea in lineas:
    print(linea)
archivo.close()
