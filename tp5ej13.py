################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from errores import IngresoIncorrecto

def buscar_palabra(texto, palabra):
    lista_palabras = texto.split()                     
    palabra = palabra.lower()                          
   
    for i in range (len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].lower()  
        if lista_palabras[i] == palabra:               
            posicion = i+1
            return posicion                            
        
    raise IngresoIncorrecto(f'"{palabra}" No se encuentra en el texto')


def prueba():
    texto = input('Digite su texto: ')
    palabra = input('Digite una palabra para buscar en el texto: ')
    resultado = buscar_palabra(texto, palabra)
    print(f'Su palabra se encuentra en la posicion: {resultado}')
    
    
if __name__ == "__main__":
    prueba()