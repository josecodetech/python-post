# Creacion diccionario
diccionarioVacio = {}
# tambien
diccionario2 = dict(a=3, b=45, c=23, d=99)
print(diccionario2)
alumno = {
    "nombre": 'Jose',
    "apellidos": 'Ojeda',
    "nota": 8
}
# Acceso
print(alumno['nombre'])
# Modificacion
alumno['nota'] = 7
print(alumno)
# Borrado
print(diccionarioVacio)
del diccionarioVacio
# Ahora daria error, lo comento
# print(diccionarioVacio)

# mostramos claves / valor
print("*"*50)
print(alumno.items())
print("*"*50)
print(alumno.keys())
print("*"*50)
print(alumno.values())
print("*"*50)
# recorrido por bucle
for clave, valor in alumno.items():
    print(clave+" = "+str(valor))
# ordenar
print("*"*50)
print(alumno)
print(sorted(alumno))
print(sorted(alumno, reverse=True))
# busqueda
print('nota' in alumno)
print('edad' in alumno)
