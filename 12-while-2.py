# OTROS EJEMPLOS CON WHILE

numero = 0

# while numero <= 5:
#     print(numero)
#     numero += 1 # Incremento para evitar un loop infinito

# IF DENTRO DEL WHILE
while numero <= 10:
    if numero == 5:
        print('Cinco')
        break
    else: 
        print(numero)
    numero += 1
    