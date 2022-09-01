import json
alumno01 = ['Jose', 8]
alumno02 = ['M Mar', 9]
alumnos = [alumno01, alumno02]
# grabar
with open("archivo.json", "w") as f:
    f.write(json.dumps(alumnos, indent=2))

# leer
with open("archivo.json", "r") as f:
    alumnos = json.loads(f.read())
print(alumnos)
