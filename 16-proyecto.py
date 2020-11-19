# PROYECTO DEL CURSO

import os

CARPETA = 'contactos/'  # Directorio de Contactos
EXTENSION = '.txt'      # Extensión de los archhivos

# CONTACTOS
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

# FUNCIÓN PRINCIPAL
def app():
    # Comprobar si el directorio existe o no
    crear_directorio()

    # Mostrar el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        try:
            opcion = int(opcion)
            # Ejecutar las opciones          
            if opcion == 1:
                agregar_contacto()
                preguntar = False
            elif opcion == 2:
                editar_contacto()
                preguntar = False
            elif opcion == 3:
                mostrar_contactos()
                preguntar = False
            elif opcion == 4:
                buscar_contacto()
                preguntar = False
            elif opcion == 5:
                eliminar_contacto()
                preguntar = False
            elif opcion == 0:
                print('Gracias por usar la aplicación')
                preguntar = False           
            else:
                opcion = str(opcion)
                print('Opción no válida, inténtelo de nuevo')
        except ValueError:
            print('Opción no válida, debe ser un número')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)

def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    print('0) Salir')

def existe_contacto(nombre):
     return os.path.isfile(CARPETA + nombre + EXTENSION)

def agregar_contacto():
    print('Escriba los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Resto de los campos
            telefono_contacto = input('Agregue el Teléfono:\r\n')
            categoria_contacto = input('Agregue la Categoría:\r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r')
            archivo.write('Teléfono: ' + contacto.telefono + '\r')
            archivo.write('Categoría: ' + contacto.categoria + '\r')

            # Cerrar el archivo
            archivo.close()

            # Mostrar un mensaje de éxito
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('El contacto ya existe \r\n')

    # Reiniciar la app
    app()

def editar_contacto():
    print('Escriba el nombre del Contacto a editar')
    nombre_anterior = input('Nombre del Contacto que desea editar: \r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            # Resto de los campos
            nombre_contacto = input('Agregue el nuevo Nombre:\r\n')
            telefono_contacto = input('Agregue el nuevo Teléfono:\r\n')
            categoria_contacto = input('Agregue la nueva Categoría:\r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r')
            archivo.write('Teléfono: ' + contacto.telefono + '\r')
            archivo.write('Categoría: ' + contacto.categoria + '\r')

            archivo.close()

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, 
            CARPETA + nombre_contacto + EXTENSION)

            # Mostrar un mensaje de éxito
            print('\r\n Contacto editado Correctamente \r\n')
    else:
        print('Ese contacto no existe\r\n')
    
    # Reiniciar la app
    app()

def mostrar_contactos():
    # Litar los ficheros de un directorio
    archivos = os.listdir(CARPETA)

    # Validar que son archivos txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    print('Tu listado de contactos: \r')    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprimir un separador entre contactos
            print('\r')

    # Reiniciar la app
    app()

def buscar_contacto():
    nombre = input('\r\nNombre del Contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\nInformación del Contacto: \r')
            for linea in contacto:
                print(linea.rstrip())
            print('\r')
    except IOError:
        print('El archivo no existe\r\n')
        print(IOError)

    # Reiniciar la app
    app()

def eliminar_contacto():
    nombre = input('\r\nNombre del Contacto que desea eliminar: \r\n')   

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente\r\n')
    except IOError: 
        print('El contacto no existe\r\n')

    # Reiniciar la app
    app()

app()
