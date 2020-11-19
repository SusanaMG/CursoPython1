# MANEJO DE FICHEROS
# Crear y escribir datos en un fichero
# w es escritura. Si no existe el fichero, lo creará. 


def app():
    # Creae el archivo
    archivo = open('archivo.txt', 'w')

    # Generar números en archivo
    for i in range(0, 20):
        archivo.write('Esta es la línea ' + str(i) + '\r')

    # Cerrar el archivo
    archivo.close()
    
app()




