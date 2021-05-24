################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import no_numero_no_positivo

def numeros_perfectos(numero):
    i = 2
    suma = 1                #asumimos que todos tienen divisor 1

    while numero > i :
        if numero % i == 0:       
            suma += i       # sumamos los divisores
        i += 1    
     
    if (suma == numero) and (numero != 1):
        return True
    else:
        return False
    

def prueba():
    numero = input('Ingrese un numero entero positivo para saber si es perfecto: ')
    numero = no_numero_no_positivo(numero)
    
    num = numeros_perfectos(numero)
    if num == True:
        print('Es perfecto')
    else:
        print('No es perfecto')
        

if __name__ == "__main__":
    prueba()