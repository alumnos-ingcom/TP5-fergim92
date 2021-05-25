################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int_positivo

def fibonacci(numero):
    serie = [1,1]
    for i in range(numero -2):
        serie.append(serie[-1] + serie[-2])

    n_esimo = serie[numero -1]                           ##ultimo elemento elejido por el usuario
    return n_esimo


def prueba():
    numero = input('Ingrese un numero entero positivo para calcular su serie fibonacci (mayor a 2): ')
    numero = convierte_a_int_positivo(numero)
    
    while numero < 3:
        numero = input('Mayor a 2!!!: ')
        numero = convierte_a_int_positivo(numero)
        
    print(fibonacci(numero))
    

if __name__ == "__main__":
    prueba()
        
        
        
        
        
        