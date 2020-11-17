# CÓDIGO CONDICIONAL
# Operadores para evaluar una operación en Pyhton

# Revisar si una condición es mayor a
balance = 500
if balance > 0:
    print('Puedes pagar')

balance2 = 0
if balance2 > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

# Likes
likes = 200
if likes == 200:
    print('Excelente, 200 likes')
else:
    print('Casi llegas a los 200')

likes2 = 200
if likes2 >= 200:
    print('Excelente, 200 likes')
else:
    print('Casi llegas a los 200')

# IF con texto
lenguaje = 'Python'
if lenguaje == 'Python':
    print('Excelente decisión')

color = 'Blanco'
if not color == 'Blanco':
    print('No es de color blanco')
else:
    print('Es de color blanco')

# Evaluar un Boolean
usuario_autenticado = True
if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')


# IF ANIDADOS
# Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

if 'PHP' in lenguajes:
    print('PHP sí existe')
else:
    print('No, no está en la lista')

# If anidados
usuario_autenticado = True
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')
