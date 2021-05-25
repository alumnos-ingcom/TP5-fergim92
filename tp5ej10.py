# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int_positivo, convierte_a_int

def convertir_a_binario(numero):
    en_binario = []
    
    if numero == 0:
        en_binario = ['0']
        
    while numero >= 1:
        resto = numero % 2
        resto = str(resto)
        en_binario.insert(0, resto)    
        numero //= 2
            
    entero_en_binario = "".join(en_binario)
    return entero_en_binario


def convertir_a_entero(numero):
    suma = 0
    numero = numero.replace(" ", "")
    
    potencias = (len(numero)) -1      
    largo = len(numero)
    
    for i in range(largo):
        num = convierte_a_int(numero[i])  ##comprobamos que hayan pasado numeros en el texto ingresado
        convertir = num * (2 **(potencias - i))
        suma += convertir
    
    return suma


def prueba():
    numero = input('Ingrese un numero entero positivo para convertirlo a binario: ')
    numero = convierte_a_int_positivo(numero)
    binario = convertir_a_binario(numero)
    print(f'Su numero en binario es: {binario}')

    numero = input('\nIngrese un numero en binario para convertirlo a entero: ')
    entero = convertir_a_entero(numero)
    print(f'Su numero en base decimal es: {entero}')


if __name__ == "__main__":
    prueba()
    
    