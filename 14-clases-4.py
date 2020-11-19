# PROGRAMACIÓN ORIENTADA A OBJETOS
# HERENCIA: puedes crear una clase que sea hija o una copia de otra. Al heredar una clase tendrás todos
# los atributos de la clase padre en la hija y podrás modificarlos en caso de ser necesario

class Restaurante():
    
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


# Crear una clase hija de Restaurante
class Hotel(Restaurante):

    # Constructor (de una clase que hereda)
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Palace', '5 Estrellas', 200)
hotel.mostrar_informacion()
