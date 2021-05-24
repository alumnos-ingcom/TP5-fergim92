################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    pass

def no_numero_int(numero):
    try:
        numero = int(numero)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{numero}" No era un número entero!',err) from err
    return numero


def no_numero_float(numero):
    try:
        numero = float(numero)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{numero}" No era un número!',err) from err
    return numero

    
def no_numero_no_positivo(numero):    
    try:
        numero = int(numero)
    except ValueError as err:
        raise IngresoIncorrecto(f'"{numero}" No era un número entero!!!', err) from err
    if numero < 0:
        raise IngressoIncorrecto(f'"{numero}" Entero positivo !!!', err)
    
    return numero

