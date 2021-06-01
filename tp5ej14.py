################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int_positivo

def capicua(numero):
    return str(numero) == str(numero)[::-1]
        
   

def prueba():
    numero = input('Ingrese un numero entero (mas de 1 cifra) para saber si es capicua: ')
    numero = convierte_a_int_positivo(numero)
    while numero < 10:
        numero = input('Mayor a 1 cifra: ')
        numero = convierte_a_int_positivo(numero)
        
    resultado = capicua(numero)
    
    if resultado == True:
        print('Es capicua')
    else:
        print('No es capicua')

             
if __name__ == "__main__":
    prueba()