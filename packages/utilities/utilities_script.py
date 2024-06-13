import os
from ..core import core_script as cs

def isEmpty(lista):
    '''
        Funcion que devuelve True o False dependiendo de la condicion si la lista entrada como parametro se encuentra
        sin datos

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    return len(lista) == 0

def limpiarPantalla():
    '''
        Funcion que simplemente llama un método de la libreria 'os' para limpiar la consola

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    os.system('cls')

def showDestinos(listaDestinos):
    '''
        Funcion que entra con parametro una lista de diccionarios(destinos) que esta muestra todos sus datos dentro de ella.

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    # Comprobar si la lista esta vacia
    if isEmpty(listaDestinos):
        print("\n<---((( No se han encontrado destinos en la base de datos )))--->\n")
    else:
        posicion = 1
        limpiarPantalla()
        # Mostrar los datos dentro de la listaDestinos por cada destino
        for destino in listaDestinos:
            print(f"{posicion}. Nombre destino: {destino['nombre']} ({destino['codigo']}) | Precio: {destino['precio']}€")
            posicion += 1
    print("\n")

def showCustomers(listaCustomers):
    '''
        Funcion que entra como parametro una lista de diccionarios(clientes) que esta muestra todos sus datos dentro de ella

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    # Comprobar si la lista esta vacia
    if isEmpty(listaCustomers):
        print("\n<---((( No se han encontrado clientes en la base de datos )))--->\n")
    else:
        limpiarPantalla()
        # Mostrar los datos dentro de la listaCustomers por cada cliente
        for customer in listaCustomers:
            print(f"ID: {customer['ID']} | Nombre cliente: {customer['nombre']}")
    print("\n")

def showBookings(listaBookings, listaCustomers, listaDestinos):
    '''
        Funcion que entra como parametros 3 lista de diccionarios(reservas, clientes, destinos) que esta muestra todos sus datos dentro de ellas
        Además con los datos de las reservas se buscan los datos correspondientes al cliente y destino registrados en la reserva
        para también mostrarlos como información adicional

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    # Comprobar si la lista esta vacia
    if isEmpty(listaBookings):
        print("\n<---((( No se han encontrado reservas en la base de datos )))--->\n")
    else:
        posicion = 1
        limpiarPantalla()
        # Mostrar los datos dentro de la listaBookings por cada reserva además de adjuntar información adicional de clientes y destinos
        for reserva in listaBookings:
            for cliente in listaCustomers:
                if cliente['ID'] == reserva['ID']:
                    nombreCliente = cliente['nombre']
            for destino in listaDestinos:
                if destino['codigo'] == reserva['codigo']:
                    nombreDestino = destino['nombre']
                    precioDestino = destino['precio']
            print(f"{posicion}. Reserva a nombre: {reserva['ID']}.{nombreCliente} | Destino: {nombreDestino} ({reserva['codigo']}) | Precio: {precioDestino}€")
            posicion += 1
    print("\n")

def showDestCodes(listaDestinos):
    '''
        Función que entra como parametro 1 lista de diccionarios(destinos) que esta muestra unicamente el código de destino y
        el nombre del destino, para dar interfaz y apoyo al usuario para seleccionar la información que necesite en el
        momento que se precise. Por ejemplo para realizar una reserva y que te muestre todos los destinos existentes

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    # Comprobar si la lista esta vacia
    if isEmpty(listaDestinos):
        print("\n<---((( No es posible mostrar la información )))--->\n")
    else:
        print("Lista códigos destinos:")
        # Mostrar los datos dentro de la listaDestinos por cada destino sin mostrar precio
        for destino in listaDestinos:
            print(f"{destino['nombre']}({destino['codigo']}),", end=" ")
        print("\n")