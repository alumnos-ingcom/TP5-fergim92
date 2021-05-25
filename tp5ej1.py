################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int

def par_impar(numero):
    while numero > 0:
            numero -= 2
            
    while numero < 0:
            numero += 2
            
    if numero == 0:
        return True
    else:
        return False
   

def prueba():
    numero = input('Ingrese un numero entero para saber si es par o impar: ')
    numero = convierte_a_int(numero)
    
    resultado = par_impar(numero)
    if resultado == True:
        print(f'El numero es par')
    else:
        print(f'El numero es impar')
  
             
if __name__ == "__main__":
    prueba()