#mcm
def dameNumeros():
    numero1 = int(input("\Dime un numero positivo ->"))
    numero2 = int(input("\Dime otro numero positivo ->"))
    return numero1, numero2
def minimoComunMultiplo(numero1,numero2):
    if numero1 > 0 and numero2 > 0:
        if numero1 >= numero2:
            mcm = numero1 * 2
            numero = numero1
        else:
            mcm = numero2 * 2
            numero = numero2
        while mcm % numero1 != 0 or mcm % numero2 != 0:
            mcm += numero
        print(f'\nEl mcm de {numero1} y {numero2} es = {mcm}')
    else:
        print("Los datos indicados no son correctos, deben ser numeros positivos.")
if __name__=='__main__':
    numero1, numero2 = dameNumeros()
    minimoComunMultiplo(numero1,numero2)