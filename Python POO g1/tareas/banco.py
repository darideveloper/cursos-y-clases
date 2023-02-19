class Banco:
    def __init__(self, name: str):
        """ Contructor de la clase

        Args:
            name (str): nombre del banco
        """

        self.name = name
        self.clientes = {}
        self.type_accounts = ["Cuenta A", "Cuenta B", "Cuenta C"]

    def add_client(self, nombre: str, edad: int, saldo_inicial: int, tipo_cuenta: str):
        """ Añadir un cliente al sistema

        Args:
            nombre (str): nombre del cliente 
            edad (int): edad del cliente
            saldo_inicial (int): monto de aperta de cuenta del cliente
            tipo_cuenta (str): tipo de cuenta aselecciondo por el cliente
        """

        client_data = {
            "edad": edad,
            "saldo": saldo_inicial,
            "tipo_cuenta": tipo_cuenta
        }
        self.clientes[nombre] = client_data

    def del_client(self, nombre:str):
        """ Eliminar un cliente por nombre

        Args:
            nombre (str): nombre del cliente a borrar
        """
        
        pass

    def update_client(self, nombre: str, edad: int, saldo: int):
        """ Actualizar edad o saldo de un cliente, por nombre

        Args:
            nombre (str): nombre del cliente de la actualización de datos
            edad (int): nueva edad del cliente
            saldo (int): nuevo saldo del cliente
        """
        pass

    def query_client(self, nombre):
        """ Mostrar información de un cliente en específico del banco """
        pass

    def query_clients(self):
        """ Mostrar información de todos los clientes del banco """

        for name, client_data in self.clientes.items():
            print (name)
            
            for key, value in client_data.items():
                print (f"\t{key}: {value}")
        

    def depositar_cliente(self, nombre:str, cantidad:float):
        """ Añadir dinero a la cuenta de un cliente

        Args:
            nombre (str): nombre del cliente a añadir dinero
            cantidad (float): dinero a añadir
        """
        pass

    def retirar_cliente(self, nombre:str, cantidad:float):
        """ retirar dinero a la cuenta de un cliente

        Args:
            nombre (str): nombre del cliente a retirar dinero
            cantidad (float): dinero a retirar
        """        
        pass


bancoppel = Banco("bancoppel")
bancoppel.add_client("dari", 23, 10, "Cuenta A")
bancoppel.add_client("Martin", 30, 1000, "Cuenta C")
bancoppel.add_client("Josue", 18, 800, "Cuenta B")
bancoppel.query_clients()
