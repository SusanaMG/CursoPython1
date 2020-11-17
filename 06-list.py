# ARRAYS O LIST

meses = ["Enero", "Febrero", "Marzo"]

lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

# Los arrays (list) comienzan en la posición 0
print(lenguajes[0]) #Python

# Ordenar los elementos
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy apendiendo {lenguajes[3]}' # Para mezclar String con variables se usa la f
print(aprendiendo)

# Modificando valores de un arreglo (list)
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar elementos a un arreglo (list)
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar elementos a un arreglo (list)
del lenguajes[1]
print(lenguajes)

# Eliminar elementos a un arreglo (list)
lenguajes.pop() # Eliminar el último elemento por defecto
print(lenguajes)

# Eliminar con pop una posición específica de un arreglo (list)
lenguajes.pop(0) # Eliminar el elemento de la posición indicada
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)
