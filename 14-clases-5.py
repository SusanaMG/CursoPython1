# PROGRAMACIÓN ORIENTADA A OBJETOS
# POLIMORFISMO: es la habilidad de tener diferentes comportamientos basada en qué subclase se está 
# utilizando, relacionado muy estrechamente con Herencia

class Restaurante():
    
    # Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre            # Atributo de la clase. Default: Public
        self.categoria = categoria      # Atributo de la clase
        self.precio = precio          # Atributo de la clase. PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}')

# GETTERS Y SETTERS - Get: obtiene un valor - Set: agrega un valor
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio 


# Crear una clase hija de Restaurante
class Hotel(Restaurante):

    # Constructor (de una clase que hereda)
    def __init__(self, nombre, categoria, precio, piscina):
        super().__init__(nombre, categoria, precio)
        self.piscina = piscina
    
    # Reescribir un método (debe llamarse igual)
    # Deben ser atributos public
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Piscina: {self.piscina}')

    # Agregar un métoto que solo exista en Hotel
    def get_piscina(self):
        return self.piscina

hotel = Hotel('Palace', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
piscina = hotel.get_piscina()
print(piscina)
