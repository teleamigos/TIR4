"""-----------------------------------------------------------------------------
----------------------------Message Hello---------------------------------------
1.-Clase Message_Hello
2.-Define funcion para en paquetar
3.- Regresa el en paquetado
--------------------------------------------------------------------------------
                            Estructura del paquete
1.- Reservado 16 bits
2.- Htime -8 bits
3.- Willingness - 8 bits
4.- Link code- 8 bits
5.- Reservado 8 bits
6.- Link message size 8 bits
7.- Neighbor interface address - 32 bits
-----------------------------------------------------------------------------"""
import struct

class Message_Hello:
    def __init__(self):
        self.reserved1=b""
        self.Ht=0
        self.Willingness=b""
        self.LC=0
        self.reserved2=b""
        self.LMS=0
        self.NIAdd=b""
