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
6.- Link message size 16 bits
7.- Neighbor interface address - 32 bits
-----------------------------------------------------------------------------"""
from struct import *

class Message_Hello:
    def __init__(self):
        self.reserved1=pack('!H',0)
        self.Ht=2 #2 segundos
        self.Willingness={
        'WILL_NEVER'   : 0,
        'WILL_LOW'     : 1,
        'WILL_DEFAULT' : 3,
        'WILL_HIGH'    : 6,
        'WILL_ALWAYS'  : 7
        }
        self.LC=7 #b"00000110"#Define code advertising
        self.reserved2=pack('!B',0)
        self.LMS=1
        self.NIAdd=['']

    def Genera(self,Willingness,vecinos,lc):
        w=self.Willingness[Willingness]
        self.LC=lc
        Hello=self.reserved1
        W=pack('!BB',self.Ht,w)
        lms=pack('!H',self.LMS)
        Hello +=W+pack('!B',self.LC)+self.reserved2+lms
        for v in vecinos:
            V=(v+',').encode(encoding='utf-8')
            Hello+=V
        return Hello

    def Desempaqueta_Hello(self,msj):
        link_code=unpack('!B',msj[4:5])[0]
        if link_code==6:
            return ['']
        elif link_code==7:
            neighbors_adds=msj[8:].decode('utf-8').split(',')
            neighbors_adds=neighbors_adds[:len(neighbors_adds)-1]
            return neighbors_adds
