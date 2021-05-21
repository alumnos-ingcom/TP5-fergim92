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
    
    else:
        while numero < 0:
            numero += 2
        if numero == 0:
            return True
        else:
            return False
   

def prueba():
    numero = input('Ingrese un numero entero para saber si es par o impar: ')
    try:
        numero = int(numero)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{numero}" No era un número entero!') from err
    
    resultado = par_impar(numero)
    if resultado == True:
        print(f'El numero es par')
    else:
        print(f'El numero es impar')
  
             
if __name__ == "__main__":
    prueba()