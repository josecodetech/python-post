paises = {'ESP','FRA','ING','ITA','POR','ALE'}
tamaño = len(paises)
print(f'Longitud del conjunto = {tamaño}')
print('HOL' in paises)

# añadir
paises.add('HOL')
print(paises)
paises.add('BEL')
print(paises)

# actualizar
# FRA no entraria, no repetidos
paises.update({'MEX','COL','ARG','FRA'})
print(paises)

# borrar
paises.remove('ESP')
print(paises)
paises.discard('ING')
print(paises)
paises.clear()
print(paises)
