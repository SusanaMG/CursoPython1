# PROGRAMACIÓN ORIENTADA A OBJETOS

class Restaurante:

    def agregar_restaurante(self, nombre):
        self.nombre = nombre # Atributo de la clase

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

# Instanciar la clase
restaurante = Restaurante()
restaurante.agregar_restaurante('Traviata')
restaurante.mostrar_informacion()

restaurante2 = Restaurante()
restaurante2.agregar_restaurante('La buena mesa')
restaurante2.mostrar_informacion()

# Mostrar la información
print(f'Nombre restaurante: {restaurante.nombre}')
print(f'Nombre restaurante: {restaurante2.nombre}')




