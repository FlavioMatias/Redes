from socket import *
from textwrap import *
from Sistema import System as sys

class Server:
    __protocols = {
        "TCP": SOCK_STREAM,
        "UDP": SOCK_DGRAM
    }

    @classmethod
    def config(cls, port : int, ip : str = "0.0.0.0", protocol : str = "TCP", backlog : int = 50):

        if ip.lower() == "localhost":
            ip = "127.0.0.1"

        protocol = cls.__protocols.get(protocol.upper())
        cls.__soc = socket(AF_INET, protocol)

        cls.__soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        cls.__soc.bind((ip, port))

        cls.__soc.listen(backlog)

        cls.__header = dedent(f'''
        Servidor ligado
        ──────────────────────────────
        porta: {port}
        host: {ip}
        ──────────────────────────────
        ''')

    @classmethod
    def ligar(cls):
        print(cls.__header)
        while True:
            try:
                cliente, address = cls.__soc.accept()
                msg = cliente.recv(128).decode("utf-8")
                retorno = sys.comando(msg)
                cliente.send(bytes(retorno,"utf-8"))
                cliente.close()

            except Exception as e:
                print(f"{address[0]} teve um erro: {e}")
                if cliente:
                    cliente.send(bytes("Erro no servidor", "utf-8"))

