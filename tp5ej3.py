################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import no_numero_no_positivo
def tribonacci(numero):
    serie = [1,1,1]
    for i in range(numero -3):
        serie.append(serie[-1] + serie[-2] + serie[-3])
     
    n_esimo = serie[numero -1]                                 ##ultimo elemento elejido por el usuario
    return n_esimo


def prueba():
    numero = input('Ingrese un numero entero positivo para calcular su serie tribonacci (mayor a 3): ')
    numero = no_numero_no_positivo(numero)
    
    while numero < 4:
        numero = input('Mayor a 3!!!: ')
        numero = no_numero_no_positivo(numero)
        
    print(tribonacci(numero))
    

if __name__ == "__main__":
    prueba()
        