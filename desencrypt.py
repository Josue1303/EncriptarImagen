#Bloque de manejo de errores en caso de que un dato se ponga mal

try:
    #Se ingresan con inputs la dirección de la imagen y la llave
    path = input(r'Ingresa la dirección de la imagen : ')
    key = int(input('Ingresa la llave de desencriptación de la imagen : '))
     
    # Se imprimen los datos para verficar que ingresamos correctamente los datos
    print('Dirección de la imagen : ', path)
    print('La llave de encriptación como de desencriptación deben de ser las mismas')
    print('Llave de desencriptación : ', key)
     
    # Se lee el archivo
    lecturaImagen = open(path, 'rb')
     
    # storing image data in variable "image"
    imagen = lecturaImagen.read()
    lecturaImagen.close()
     
    # converting image into byte array to perform decryption easily on numeric data
    imagen = bytearray(imagen)
 
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(imagen):
        imagen[index] = values ^ key
 
    # opening file for writing purpose
    escrituraImagen = open(path, 'wb')
     
    # writing decryption data in image
    escrituraImagen.write(imagen)
    escrituraImagen.close()
    print('Decryption Done...')
 
 
except Exception:
    print('Error caught : ', Exception.__name__)

    #Barcelona Geeks (2022, 5 julio). Cifrar y descifrar imágenes usando Python – Barcelona Geeks. https://barcelonageeks.com/encriptar-y-desencriptar-una-imagen-usando-python/