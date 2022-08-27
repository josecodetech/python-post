# creacion
lista = []
# puede contener distintos tipos de datos
alumno01 = ['Jose', 8]
alumno02 = ['M Mar', 9]
alumnos = [alumno01, alumno02]
print(alumnos)
# añadir dato con insert se indica posicion
alumnos.append(['Lucia', 10])
alumnos.insert(1, ['Eva', 10])
print(alumnos)
# mostrar parte de la lista, slicing
print(alumnos[2:])
# modificar dato en la posicion indicada
alumnos[2][1] = 10
print(alumnos)
# borrar un elemento por posicion
del alumnos[0]
print(alumnos)
alumnos.pop()
print(alumnos)
# tamaño y ordenar
alumnos.append(['Lucia', 10])
alumnos.append(['Jose', 7])
print(len(alumnos))
print(alumnos)  # antes de ordenar
alumnos.sort()
print(alumnos)  # despues de ordenar
# recorrer lista
for alumno in alumnos:
    print(f"Nombre: {alumno[0]}")
    print("*"*50)
# busqueda
print(["Jose", 7] in alumnos)
