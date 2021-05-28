################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from errores import IngresoIncorrecto

def buscar_palabra(texto, palabra):
    lista_palabras = texto.split()                     ##separamos el texto en sus palabras y los guardamos en una lista
    palabra = palabra.lower()                          ##ignoramos las mayusculas solo buscamos que las palabras coincidan
   
    for i in range (len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].lower()  ## ignoramos las mayusculas del texto
        if lista_palabras[i] == palabra:               ##comparamos cada elemento de la lista con la palabra que buscamos
            posicion = i+1
            return posicion                            ## si coinciden retornamos la posicion de la coincidencia
        
    raise IngresoIncorrecto(f'"{palabra}" No se encuentra en el texto') ## si no encontramos la palabra el ultimo paso es levantar una excepcion


def prueba():
    texto = input('Digite su texto: ')
    palabra = input('Digite una palabra para buscar en el texto: ')
    resultado = buscar_palabra(texto, palabra)
    print(f'Su palabra se encuentra en la posicion: {resultado}')
    
    
if __name__ == "__main__":
    prueba()