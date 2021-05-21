################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def tribonacci(termino):
    serie = [1,1,1]
    for i in range(termino -3):
        serie.append(serie[-1] + serie[-2] + serie[-3])
    return serie


def prueba():
    termino = input('Ingrese un numero entero positivo para calcular su serie tribonacci (minimo 3): ')
    try:
        termino = int(termino)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{termino}" No era un número entero!!!') from err
    if termino <= 2:
        raise IngresoIncorrecto(f'"{termino}" Entero positivo y mayor a 2!!!')
    
    print(tribonacci(termino))
    

if __name__ == "__main__":
    prueba()
        