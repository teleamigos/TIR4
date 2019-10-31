"""-----------------------------------------------------------------------------
---------------------------------TC clase---------------------------------------
1.- Inicializacion
2.- Empaquetado
3.- Desmepaquetado
--------------------------------------------------------------------------------
                            Estructura del paquete

1.- ANSN - 16 bits
2.- Reservado - 16 bits
3.- ANMA -32 bits

-----------------------------------------------------------------------------"""
from struct import*
class Message_TC:
    def __init__(self):
        self.ANSN=pack('!H',0)
        self.reserved=pack('!H',0)
        self.ANMA=[]
    def Genera(self,vecinos):
        TC=pack('!H',0)+self.reserved
        for v in vecinos:
            V=(v+',').encode(encoding='utf-8')
            TC+=V
        return TC

    def Desempaqueta__TC(self,msj):
        neighbors_adds=msj[4:].decode('utf-8').split(',')
        neighbors_adds=neighbors_adds[:len(neighbors_adds)-1]
        return neighbors_adds
