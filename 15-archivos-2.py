# MANEJO DE FICHEROS
# Mostrar el contenido de un fichero en la terminal

def app():
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())

app()
