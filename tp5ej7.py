################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_float

def distancia_entre_puntos(n1, n2):
    centro = (n1 + n2) / 2
    radio = (n2 - n1) / 2
    
    if radio < 0:
        distancia = radio * -2
    else:
        distancia = radio * 2
    
    return distancia

def prueba():
    print('Ingrese dos numeros para conocer la distancia entre ellos')
    n1 = input('Numero 1: ')
    n1 = convierte_a_float(n1)
    
    n2 = input('Numero 2: ')
    n2 = convierte_a_float(n2)
    
    dist = distancia_entre_puntos(n1, n2)
    print(f'La distancia es: {dist}')
    
    
if __name__ == "__main__":
    prueba()