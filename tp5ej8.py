################
# Gimenez Fernando - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from errores import convierte_a_int

def cifrado(texto, mover):
    codificado = []
    
    for letra in texto:
        if letra == " ":
            codificado.append(" ")
            continue
        numero_letra = ord(letra)
        numero_letra_modi = numero_letra + mover
        letra_modi = chr(numero_letra_modi)
        codificado.append(letra_modi)
        
    texto = "".join(codificado)  #convertimos la lista en string
    return texto

def decifrado(texto, mover):
    codificado = []
    
    for letra in texto:
        if letra == " ":
            codificado.append(" ")
            continue
        numero_letra = ord(letra)
        numero_letra_modi = numero_letra - mover
        letra_modi = chr(numero_letra_modi)
        codificado.append(letra_modi)
        
    texto = "".join(codificado)  #convertimos la lista en string
    return texto
    
    
def prueba():
    texto = input('Digite un texto para codificarlo: ')
    mover = input('Cuantas posiciones desea rotar el abecedario para cifrar el mensaje: ')
    mover = convierte_a_int(mover)
    
    texto_cifrado = cifrado(texto, mover)
    texto_decifrado = decifrado(texto_cifrado, mover)
    
    print(f'Mensaje cifrado: {texto_cifrado}')
    print(f'Mensaje decifrado: {texto_decifrado}')
                            
    
if __name__ == "__main__":
    prueba()