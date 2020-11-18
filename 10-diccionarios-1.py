# OBJETOS (DICCIONARIOS EN PYTHON)

# Creando un diccionario simple
cancion = {
    'artista' : 'Metallica',  # llave y valor
    'cancion' : 'Enter Sandman', 
    'lanzamiento' : 1992, 
    'likes' : 3000
}

print(cancion)

# Acceder a los elementos del diccionario
print(cancion['artista'])

# Mezclar con un string (mejor asignar a una variable para que no dé error)
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

print(cancion)

# Agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# Reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

# Eliminar valor existente
del cancion['lanzamiento']
print(cancion)
