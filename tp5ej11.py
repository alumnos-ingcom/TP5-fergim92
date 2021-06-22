################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int

def promedio_movil(numeros):
    suma_numeros = 0
    promedio = []
    for numero in numeros:
        suma_numeros += numero
    
    cantidad_de_numeros_lista = len(numeros)
    promedio_general = suma_numeros / cantidad_de_numeros_lista
    promedio_general = round(promedio_general, 2)
    promedio.append(promedio_general)
    
    return promedio


def prueba():
    numeros = []
    cantidad_de_numeros_lista = input('Cuantos numeros tendra su lista: ')
    cantidad_de_numeros_lista = convierte_a_int(cantidad_de_numeros_lista)
    
    for i in range(cantidad_de_numeros_lista):
        numero = input(f'{i+1})Ingrese el numero: ')
        numero = convierte_a_int(numero)
        numeros.append(numero)
    
    resultado = promedio_movil(numeros)
    print(f'El promedio de su lista es de: {resultado}')
    
    
if __name__ == "__main__":
    prueba()
    
    