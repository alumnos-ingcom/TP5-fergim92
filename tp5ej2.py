################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def fibonacci(termino):
    serie = [1,1]
    for i in range(termino -2):
        serie.append(serie[-1] + serie[-2])
    return serie


def prueba():
    termino = input('Ingrese un numero entero positivo para calcular su serie fibonacci (minimo 2): ')
    try:
        termino = int(termino)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{termino}" No era un número entero!!!') from err
    if termino <= 1:
        raise IngresoIncorrecto(f'"{termino}" Entero positivo y mayor a 1!!!')
    
    print(fibonacci(termino))
    

if __name__ == "__main__":
    prueba()
        
        
        
        
        
        