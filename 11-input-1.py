# ENTRADA DE DATOS POR PARTE DEL USUARIO

nombre = input('¿Cuál es tu nombre?: \r\n ')

print(f'Hola {nombre}')

# Leer datos que serán números
edad = input('¿Cuál es tu edad?: \r\n ') 
# Convertir edad (string) a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else: 
    print('Aún no puedes votar')

# Mezclar con operadores
numero = input('Agrega un número y te diré si es par o impar: \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')


# Reto
''' Realiza un examen con 3 preguntas que tu desees. El usuario deberá responder "SI" o "NO" y al final 
otorgarle una calificación (La calificación se logra con una variavle que se inicia en 0 y por cada
respuesta correcta incrementa en 1)'''

print('Inicio del examen: responda "SI" o "NO"')

preguntas = ["¿2+2=4?", "¿9/3=3?", "¿2x3=6?"]
posicion = 0
preg = preguntas[posicion]
total = len(preguntas)
nota = 0

for pregunta in preguntas:
    respuesta = input(preg)
    if posicion < (total-1):
        posicion += 1  # posicion = posicion + 1
        preg = preguntas[posicion]
    if respuesta == "SI":
        nota += 1  # nota = nota + 1

print(f'Tu nota es {nota}')
