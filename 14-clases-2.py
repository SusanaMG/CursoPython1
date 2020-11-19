# PROGRAMACIÓN ORIENTADA A OBJETOS
# CONSTRUCTOR: es una función que se ejecuta automáticamente al crear un objeto por medio de una clase
# ABSTRACCIÓN: son los datos necesarios de una clase

class Restaurante:

    # Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre            # Atributo de la clase
        self.categoria = categoria      # Atributo de la clase
        self.precio = precio            # Atributo de la clase

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}')

# Instanciar la clase
restaurante = Restaurante('Traviata', 'Italiano', 20)
restaurante.mostrar_informacion()

restaurante2 = Restaurante('La buena mesa', 'Mediterránea', 35)
restaurante2.mostrar_informacion()




