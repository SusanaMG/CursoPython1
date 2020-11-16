# FUNCIONES CON NUMEROS

def suma1():
    print(2 + 2)

def suma2(a = 0, b = 0):    # Funcion con parámetros default
    print(a + b)

suma2(2, 3)
suma2(10, 3.5)
suma2(10)

def resta(a, b):
    print(a - b)

resta(10, 8)

def multiplicacion():
    primero = input('Meta el primer número: ')
    segundo = input('Meta el segundo número: ')
    print(int(primero) * int(segundo)) 
    ## Formas incorrectas
    # print (primero - segundo)
    # # print ({primero} - {segundo})
    # print (f'{primero} - {segundo}')
    
multiplicacion()

def mitad(a):
    print('La mitad del argumento es: ')
    print(int(a) / 2)
    b = input('¿Pon un número?: ')
    print('La mitad de tu número es ' + str((int(b) / 2)))

mitad(4)