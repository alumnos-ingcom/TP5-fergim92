################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def numeros_perfectos(numero):
    i = 2
    suma = 1                #asumimos que todos tienen divisor 1

    while numero > i :
        if numero % i == 0:       
            suma += i       # sumamos los divisores
        i += 1    
     
    if suma == numero and numero != 1:
        return True
    else:
        return False
    

def prueba():
    numero = input('Ingrese un numero entero positivo para saber si es perfecto: ')
    try:
        numero = int(numero)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{numero}" No era un número entero!!!') from err
    if numero < 0:
        raise IngresoIncorrecto(f'"{numero}" Entero positivo !!!')
    
    num = numeros_perfectos(numero)
    if num == True:
        print('Es perfecto')
    else:
        print('No es perfecto')
        

if __name__ == "__main__":
    prueba()