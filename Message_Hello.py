"""-----------------------------------------------------------------------------
----------------------------Message Hello---------------------------------------
1.-Clase Message_Hello
    *Cada campo de la trama es definida
2.-Define funcion para en paquetar
    * Se necesita ingresar previamente Willingness para empacar correctamente.
    * Regresa el mensaje de Hello Empaquetado
3.-Desempaquetado
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
from struct import *

class Message_Hello:
    def __init__(self):
        self.reserved1=b"0000000000000"
        self.Ht=2 #2 segundos
        self.Willingness={
        'WILL_NEVER'   : 0,
        'WILL_LOW'     : 1,
        'WILL_DEFAULT' : 3,
        'WILL_HIGH'    : 6,
        'WILL_ALWAYS'  : 7
        }
        self.LC=b"00000110"#Define code advertising
        self.reserved2=b"00000000"
        self.LMS=1
        self.NIAdd=b'\xff\xff\xff\xff\xff\xff'

    def Genera(self,Willingness,vecinos):
        w=self.Willingness[Willingness]
        Hello=self.reserved1
        W=pack('!BB',self.Ht,w)
        lms=pack('!H',self.LMS)
        Hello +=W+self.LC+self.reserved2+lms+self.NIAdd
        for v in vecinos:
            V=v.encode(encoding='utf-8')
            Hello+=V
        return Hello
