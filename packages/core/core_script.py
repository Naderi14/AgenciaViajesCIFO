from ..utilities import utilities_script as us

listaDestinos = []
listaCustomers = []
listaBookings = []

def AddDestino():
    '''
        Funcion que sirve para agregar un nuevo destinoa raiz de 3 inputs para formar un diccionario 
        del nuevo destino y agregarlo a la lista.

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    # Input codigo destino con su control de entrada
    while True:
        esNumero = True
        codigoDestino = input("Introduzca el código identificativo del nuevo destino ---> : ").upper()
        try:
            int(codigoDestino)
        except:
            esNumero = False
        if codigoDestino == None or codigoDestino.strip() == "" or esNumero == True:
            print("\n<---((( ¡¡El código no puede quedar vacío y tampoco ser un número!! )))--->\n")
        else:
            break
    # Input nombre destino con su control de entrada
    while True:
        esNumero = True
        nameDestino = input("Introduzca el nombre del nuevo destino ---> : ").title()
        try:
            int(nameDestino)
        except:
            esNumero = False
        if nameDestino == None or nameDestino.strip() == "" or esNumero == True:
            print("\n<---((( ¡¡El nombre del destino no puede quedar vacío y tampoco ser un número!! )))--->\n")
        else:
            break
    # Input precio destino con su control de entrada
    while True:
        precioDestino = input("Introduzca el precio del nuevo destino ---> : ")
        try:
            precioDestino = round(float(precioDestino),2)
            if precioDestino <= 0:
                print("\n<---((( ¡¡El precio tiene que ser mayor que 0!! )))--->\n")
            elif precioDestino > 999999.99:
                print("\n<---((( ¡¡El precio no puede tener mas de 6 ceros!! )))--->\n")
            else:
                break
        except:
            print("\n<---((( ¡¡El precio tiene que ser un número!! )))--->\n")
    # Creamos diccionario
    nuevoDestino = {
        'codigo' : codigoDestino, #string
        'nombre' : nameDestino, #string
        'precio' : precioDestino #float
        }
    # Añadimos el diccionario a la lista
    listaDestinos.append(nuevoDestino)
    us.limpiarPantalla()
    print("<--- Destino agregado --->\n")
    
def AddCustomer():
    '''
        Función que sirve para agregar un nuevo cliente con 1 entrada input para crear un diccionario
        y agregarlo en la lista de clientes

        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    # Asignamos ID al nuevo cliente con su control de entrada
    id = len(listaCustomers) + 1
    # Input nombre cliente
    while True:
        esNumero = True
        nombreCliente = input("Introduzca el nombre del nuevo cliente ---> : ").title()
        try:
            int(nombreCliente)
        except:
            esNumero = False
        if nombreCliente == None or nombreCliente.strip() == "" or esNumero == True:
            print("\n<---((( ¡¡El nombre del cliente no puede quedar vacío y tampoco ser un número!! )))--->\n")
        else:
            break
    # Creamos diccionario
    nuevoCliente = {
        'ID' : id, #int
        'nombre' : nombreCliente #string
    }
    # Añadimos el diccionario a la lista
    listaCustomers.append(nuevoCliente)
    us.limpiarPantalla()
    print("<--- Cliente agregado --->\n")

def AddBooking():
    '''
        Función que sirve para agregar una nueva reserva con 2 entradas input para crear un diccionario y
        agregarlo en la lista de reservas
        
        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    if us.isEmpty(listaCustomers) or us.isEmpty(listaDestinos):
        print("\n<---((( No se pueden hacer reservas sin clientes o destinos en la base de datos )))--->\n")
    else:
        # Input codigo destino con su control de entrada
        codigoOK = False
        idOK = False
        us.showDestCodes(listaDestinos)
        while codigoOK == False:
            esNumero = True
            codigoDestino = input("Introduzca el código de destino ---> : ").upper()
            try:
                int(codigoDestino)
            except:
                esNumero = False
            if codigoDestino == None or codigoDestino.strip() == "" or esNumero == True:
                print("\n<---((( ¡¡El código no puede quedar vacío y tampoco ser un número!! )))--->\n")
            else:
                for destino in listaDestinos:
                    if codigoDestino == destino['codigo']:
                        codigoOK = True
                if codigoOK == False:
                    print("\n<---((( ¡¡El código no coincide con ningún destino en la base de datos!! )))--->\n")
        # Input nombre cliente con su control de entrada
        us.limpiarPantalla()
        us.showCustomers(listaCustomers)
        while idOK == False:
            idCliente = input("Introduzca el ID del cliente que realiza la reserva ---> : ").title()
            if idCliente.isnumeric():
                idCliente = int(idCliente)
                for cliente in listaCustomers:
                    if idCliente == cliente['ID']:
                        idOK = True
                        break
                if idOK == False:
                    print("\n<---((( ¡¡El ID no coincide con ningún cliente en la base de datos!! )))--->\n")
            else:
                print("\n<---((( ¡¡El ID del cliente ha de ser un valor numérico y positivo!! )))--->\n")
        # Creamos diccionario
        nuevoBooking = {
            'codigo' : codigoDestino, #string
            'ID' : idCliente #int
        }
        # Añadimos el diccionario a la lista
        listaBookings.append(nuevoBooking)
        us.limpiarPantalla()
        print("<--- Reserva agregada --->\n")
   
def CancelBooking():
    '''
        Función que sirve para cancelar/eliminar de la lista de reservas una reserva que para encontrarla
        requiere de 2 inputs
        
        Es una funcion void y por lo tanto no devuelve ningún valor y tampoco requiere argumentos
    '''
    if us.isEmpty(listaBookings):
        print("\n<---((( No se han encontrado reservas en la base de datos )))--->\n")
    else:
        # Input codigo destino con su control de entrada
        while True:
            esNumero = True
            codigoDestino = input("Introduzca el código del destino ---> : ").upper()
            try:
                int(codigoDestino)
            except:
                esNumero = False
            if codigoDestino == None or codigoDestino.strip() == "" or esNumero == True:
                print("\n<---((( ¡¡El código no puede quedar vacío y tampoco ser un número!! )))--->\n")
            else:
                break
        # Input ID Cliente con su control de entrada
        while True:
            idCliente = input("Introduzca el ID del cliente ---> : ").title()
            if idCliente.isnumeric():
                idCliente = int(idCliente)
                break
            else:
                print("\n<---((( ¡¡El ID del cliente ha de ser un valor numérico y positivo!! )))--->\n")
        # Buscamos si existe la reserva, si existe la cancelamos e informamos
        for reserva in listaBookings:
            if codigoDestino == reserva['codigo'] and idCliente == reserva['ID']:
                for cliente in listaCustomers:
                    if cliente['ID'] == reserva['ID']:
                        nombreCliente = cliente['nombre']
                for destino in listaDestinos:
                    if destino['codigo'] == reserva['codigo']:
                        nombreDestino = destino['nombre']
                        precioDestino = destino['precio']
                us.limpiarPantalla()
                print(f"<--- La reserva de {nombreCliente} para un viaje a {nombreDestino}({reserva['codigo']}) por {precioDestino}€, ha sido cancelada --->\n")
                listaBookings.remove(reserva)
            else:
                print("\n<---((( El codigo o la ID del cliente no coincide con ninguna reserva en curso )))--->\n")