from ..core import core_script as cs
from ..utilities import utilities_script as us

def Agencia_MenuPrincipal():
    '''
        Funcion que hace de menú principal del programa de gestión de la agencia de viajes.
        Proporciona en interfaz para el usuario un abanico de opciones y la llamada a cada una de las funciones
        hayadas en el aplicativo.

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    opcion = None
    us.limpiarPantalla()
    while opcion != 8:
        print("<-----=====Travel Agency Manager=====----->")
        print(
            "   1. Añadir un nuevo destino (Codigo Destino | Nombre Destino | Precio)\n"
            "   2. Añadir un nuevo cliente (Nombre Cliente)\n"
            "   3. Realizar una reserva (Codigo Destino | ID Cliente)\n"
            "   4. Cancelar una reserva (Codigo Destino | ID Cliente)\n"
            "   5. Mostrar todos los destinos\n"
            "   6. Mostrar todos los clientes\n"
            "   7. Mostrar todas las reservas\n"
            "   8. Salir de la aplicación\n"
        )
        try:
            opcion = int(input('Seleccionar opción: '))
        except ValueError:
            us.limpiarPantalla()
            print("-----=====¡¡ Dato erróneo introducido, vuelva a repetir !!=====-----\n")
        if opcion == 1:
            us.limpiarPantalla()
            cs.AddDestino()
        elif opcion == 2:
            us.limpiarPantalla()
            cs.AddCustomer()
        elif opcion == 3:
            us.limpiarPantalla()
            cs.AddBooking()
        elif opcion == 4:
            us.limpiarPantalla()
            cs.CancelBooking()
        elif opcion == 5:
            us.limpiarPantalla()
            us.showDestinos(cs.listaDestinos)
        elif opcion == 6:
            us.limpiarPantalla()
            us.showCustomers(cs.listaCustomers)
        elif opcion == 7:
            us.limpiarPantalla()
            us.showBookings(cs.listaBookings, cs.listaCustomers, cs.listaDestinos)
        elif opcion == 8:
            us.limpiarPantalla()
            print("¡Hasta la próxima!\n")
        else:
            print("Opción no válida\n")