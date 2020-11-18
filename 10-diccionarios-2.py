# OTRAS OPERACIONES CON OBJETOS (DICCIONARIOS EN PYTHON)

# iIniciar un diccionario vacío
jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'Juan'
jugador['puntuacion'] = 0
print(jugador)

# Incrementando puntuación
jugador['puntuacion'] = 100
print(jugador)

# Incrementando puntuación
jugador['puntuacion'] = 200
print(jugador)

# Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

# Iterar en el diccionario
for llave, valor in jugador.items():
    #print(llave)
    print(valor)

# Eliminar jugador y puntuación
del jugador['nombre']
del jugador['puntuacion']
print(jugador)