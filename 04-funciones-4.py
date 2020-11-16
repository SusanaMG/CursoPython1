# DIFERENCIAS ENTRE FUNCIONES Y METODOS

nombre = 'sara'

def mostrar_nombre(nombre):
    print(f'Hola {nombre}')

mostrar_nombre(nombre)

print(nombre.upper())
print(nombre.title())

# Reto: funciones

texto = 'Hola ¡bienvenida!'
nombre = 'Susana'

def saludo(mensaje):
    print(f'{mensaje}')

saludo(texto)

def saludoPersonalizado(mensaje, nombre):
    print(f'{mensaje} {nombre}')

saludoPersonalizado(texto, nombre)

def saludoPersonalizado2(mensaje, nombre):
    profesion = input("¿Cuál es tu profesión? ")
    print(f'{mensaje} {profesion} {nombre}')

saludoPersonalizado2(texto, nombre)