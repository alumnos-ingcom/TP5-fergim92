################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int

def comparar_listas(lista_1, lista_2):
    coincidencias = 0
    
    for i in range (len(lista_1)):
        for j in range (len(lista_1)):   
            if lista_1[i] == lista_2[j]:
                coincidencias += 1
    if coincidencias == len(lista_1):
        return True
    else:
        return False


def prueba():
    lista_1 = []
    lista_2 = []
    cantidad_de_numeros_lista = input('Cuantos elementos tendran sus 2 listas: ')
    cantidad_de_numeros_lista = convierte_a_int(cantidad_de_numeros_lista)
    
    for i in range(cantidad_de_numeros_lista):
        elemento_lista_1 = input(f'Elemento {i+1} de a lista (1): ')
        lista_1.append(elemento_lista_1)   
    for i in range(cantidad_de_numeros_lista):
        elemento_lista_2 = input(f'Elemento {i+1} de a lista (2): ')
        lista_2.append(elemento_lista_2)
    
    resultado = comparar_listas(lista_1, lista_2)
    if resultado == True:
        print('Las listas son iguales')
    else:
        print('Las listas no son iguales')
    
    
if __name__ == "__main__":
    prueba()