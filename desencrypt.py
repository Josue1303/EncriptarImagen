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
     
    # Se almacena la imagen en una variable imagen.
    imagen = lecturaImagen.read()
    lecturaImagen.close()
     
    # La imagen se convierte en un arreglo de bytes para poder desencriptar
    imagen = bytearray(imagen)
 
    # A cada valor del arreglo se le hace la operación XOR, este sería nuestro método de desencriptación
    for index, values in enumerate(imagen):
        imagen[index] = values ^ key
 
    # Se abre el archivo en forma de escritura
    escrituraImagen = open(path, 'wb')
     
    # Se escribe la desencriptación en la imagen
    escrituraImagen.write(imagen)
    escrituraImagen.close()
    print('Desencriptación terminada...')
 
 
except Exception:
    print('Error : ', Exception.__name__)

    #Barcelona Geeks (2022, 5 julio). Cifrar y descifrar imágenes usando Python – Barcelona Geeks. https://barcelonageeks.com/encriptar-y-desencriptar-una-imagen-usando-python/