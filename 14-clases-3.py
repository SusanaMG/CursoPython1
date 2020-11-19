# PROGRAMACIÓN ORIENTADA A OBJETOS
# ENCAPSULAMIENTO: permite restingir u ocultar el acceso a los datos dentro de la misma clase del mundo
# exterior (usualmente se modifican vía métodos en la misma clase)
# Default: Public -- self.variable -- Se puede modificar y acceder desde cualquier lugar de la aplicación
# PROTECTED -- self._variable -- Se puede modificar y acceder desde cualquier lugar de la clase
# PRIVATE -- self.__variable -- Se puede acceder y modificar por métodos GETTERS Y SETTERS

class Restaurante:
    
    # Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre            # Atributo de la clase. Default: Public
        self.categoria = categoria      # Atributo de la clase
        self.__precio = precio          # Atributo de la clase. PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.__precio}')

# GETTERS Y SETTERS - Get: obtiene un valor - Set: agrega un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio 

# Instanciar la clase
restaurante = Restaurante('Traviata', 'Italiano', 20)
# restaurante.__precio = 25  # No es posible modificarlo así porque es private
restaurante.mostrar_informacion()
restaurante.set_precio(15)
precio = restaurante.get_precio()
print(precio)

restaurante2 = Restaurante('La buena mesa', 'Mediterránea', 35)
restaurante2.mostrar_informacion()
precio2 = restaurante2.get_precio()
print(precio2)
