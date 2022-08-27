# crear funcion
def mi_funcion(parametro):
    """ Documentacion funcion
        Se puede ver con mi_funcion.__doc__
    """
    # Indentar correctamente
    resultado = parametro * 2
    return resultado


# llamada a la funcion
# y la mostramos
print(mi_funcion(3))


def suma(num1, num2):
    """Devuelve la suma de 
        2 numeros pasados por parametros
    """
    resultado = num1 + num2
    return resultado


print("="*25)
print(suma(15, 20))
print("="*25)

# funcion sin parametros


def menuOpciones():
    """Funcion sin parametros
        muestra un menu
        no devuelve valor
    """
    print("="*25)
    print("""
          Menu de opciones
          1. Sumar
          2. Restar
          3. Multiplicar
          4. Dividir
          5. Salir
          """)
    print("="*25)


# la llamo 2 veces
menuOpciones()
menuOpciones()
