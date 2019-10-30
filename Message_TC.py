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

class Message_TC:
    def __inti(self):
        self.ANSN=0
        self.reserved=b"0000000000000000"
        self.ANMA=b""

    def Genera(self,vecinos):
        TC=pack('!H',self.ANSN)+self.reserved
        for v in vecinos:
            V=v.encode(encoding='utf-8')
            TC+=V
        return TC
