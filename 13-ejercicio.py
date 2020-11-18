# CREANDO UN PROYECTO DE PLAYLIST CON WHILE, LISTAS Y DICCIONARIOS

playlist = {}  # Diccionario vacío
playlist['canciones'] = []  # Lista vacía de canciones


# Función principal
def app():
    # Agregar playlist
    agregar_playlist = True # Bandera
    while agregar_playlist:
        nombre_playlist = input('Cómo deseas nombrar la playlist? \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            # Ya tenemos un nombre, desactivar True
            agregar_playlist = False
            # Llamar a la función para agregar canciones
            agregar_canciones()

def agregar_canciones():
    # Agregar canciones
    agregar_cancion = True # Bandera
    while agregar_cancion:
        # Preguntar al usuario qué canción desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            # Dejar de gregar las canciones
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print('\r')
    print(f'Playlist: {nombre_playlist} \r')
    print('Canciones: \r')
    for cancion in playlist['canciones']:
        print(cancion)

app()
