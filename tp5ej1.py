################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def par_impar(numero):
    if numero > 0:
        while numero > 0:
            numero -= 2
        if numero == 0:
            return True
        else:
            return False
    
    elif numero < 0:
        while numero < 0:
            numero += 2
        if numero == 0:
            return True
        else:
            return False
    else:
        return 0


def prueba():
    numero = input('Ingrese un numero entero para saber si es par o impar: ')
    try:
        numero = int(numero)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{numero}" No era un número entero!') from err
    
    resultado = par_impar(numero)
    if resultado == True:
        print(f'El numero es par')
    elif resultado == False:
        print(f'El numero es impar')
    else:
        print(f'El numero es cero')
             

if __name__ == "__main__":
    prueba()