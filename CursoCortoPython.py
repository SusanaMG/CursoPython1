print("Hola Mundo 1")

# Esto es un comentario
print("Hola Mundo 2")

"""
Esto es un comentario multilinea
"""

# Variables
texto = "Repaso de Python"
nombre = "Susana"
apellido = "Márquez"
year = 2020

# Impresion por pantalla y tipos de concatenaciones
print(texto)
print("Mi nombre: " + nombre + " " + apellido)
print("Mi nombre: " + nombre + " " + apellido + " " + str(year))
print(year + year)
print(f"{year} - {year}")
print(f"{texto} - {nombre} - {year}")

# Entrada
sitioweb = input("¿Cuál es tu página web?: ")
print("Tu sitio web es: " + sitioweb)

# Condiciones
# altura = 187
altura = int(input("¿Cuál es tu altura?: "))

if altura >= 180:
    print("Eres una persona alta")
else:
    print("Eres una persona baja")

# Funciones
print("Llamada 3 veces a la misma función")
def mostrarAltura():
    altura = int(input("¿Cuál es tu altura?: "))

    if altura >= 180:
        print("Eres una persona alta")
    else:
        print("Eres una persona baja")

mostrarAltura()
mostrarAltura()
mostrarAltura()

print("Llamada 3 veces a la misma función que recibe un mismo parámetro")
var_altura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura2(altura2):
    if altura2 >= 180:
        print("Eres una persona alta")
    else:
        print("Eres una persona baja")

mostrarAltura2(var_altura)
mostrarAltura2(var_altura)
mostrarAltura2(var_altura)

print("Función con salida de datos")
var_miAltura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura3(altura):
    resultado =""

    if altura >= 180:
        resultado = "Eres una persona alta"
    else:
        resultado = "Eres una persona baja"

    return resultado

print(mostrarAltura3(var_miAltura)) 

# Listas
personas = ["Ana", "Juan", "Sara"]
print(personas)
print(personas[2])

# Bucles
for persona in personas:
    print("- " + persona)

contador = 0
for persona in personas:
    contador = contador + 1

print("Número de personas total: " + str(contador))
