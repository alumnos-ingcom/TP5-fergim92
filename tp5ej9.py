# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factorial(numero):
    i = 1
    factorial = 1
    while i < numero:
        factorial *= i+1
        i += 1
    return factorial


def factorion():
    maximo = 1499999
    lista_factoriones = []
    
    for numero in range (maximo):
        numero = str(numero)
        suma_digitos = 0
        for digito in numero:
            digito = int(digito)
            factoriales = factorial(digito)
            suma_digitos = suma_digitos + factoriales
        suma_digitos = str(suma_digitos)
        if suma_digitos == numero:
            suma_digitos = int(suma_digitos)
            lista_factoriones.append(suma_digitos)
    return lista_factoriones
            
        
def prueba():
    lista = factorion()
    print(f'Lista de factoriones\n{lista}')
      
if __name__ == "__main__":
    prueba()