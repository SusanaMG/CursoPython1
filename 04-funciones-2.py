# FUNCIONES CON PARÁMETROS Y ARGUMENTOS

def informacion(nombre, puesto = 'Desconocido'):
    print(f'Soy {nombre} y soy {puesto}')

informacion('Susana', 'Programadora')
informacion('Pedro', 'Diseñador')
informacion('Sara') # Usa el parámetro default
