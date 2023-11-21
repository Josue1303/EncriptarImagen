
#Bloque de manejo de errores en caso de que un dato se ponga mal
try:
    #Se ingresan con inputs la dirección de la imagen y la llave
    path = input(r'Ingresa la dirección de la imagen : ')
    key = int(input('Ingresa la llave de encriptación de la imagen : '))
     
    #Se imprimen los datos para verificar lo que estamos utilizando
    print('Dirección de la imagen : ', path)
    print('Llave de encriptación : ', key)
     
    # Se lee el archivo
    lecturaImagen = open(path, 'rb')
     
    # Se almacena la imagen en una variable imagen.
    imagen = lecturaImagen.read()
    lecturaImagen.close()
     
    # La imagen se convierte en un arreglo de bytes para poder encriptar
    imagen = bytearray(imagen)
 
    # A cada valor del arreglo se le hace la operación XOR, este sería nuestro método de encriptación
    for index, values in enumerate(imagen):
        imagen[index] = values ^ key
 
    # Se abre el archivo para escribir sobre el
    escrituraImagen = open(path, 'wb')
     
    # writing encrypted data in image
    escrituraImagen.write(imagen)
    escrituraImagen.close()
    print('Encriptación terminada...')
 
     
except Exception:
    print('Error : ', Exception.__name__)

 #Barcelona Geeks (2022, 5 julio). Cifrar y descifrar imágenes usando Python – Barcelona Geeks. https://barcelonageeks.com/encriptar-y-desencriptar-una-imagen-usando-python/