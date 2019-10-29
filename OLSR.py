"""-----------------------------------------------------------------------------
-------------------------------OLSR clase---------------------------------------
1.- Inicializacion
2.- Empaquetado
3.- Desempaquetado
--------------------------------------------------------------------------------
                            Estructura del paquete

1.- Longitud del paquete :16 bits
2.- Numero de secuencia del paquete-16 bits
3.- Typo de Mensaje- 8 bits
4.- Vtime -8 bits(por cuanto tiempo despues de llegado al nodo se toma la informacion)
5.- Tamaño de mensaje 16 bits
6.- Originador de Direccion -32 bits Contiene la direccion de cada nodo,NO ES IP
7.- Tiempo de vida -8 bits El numero de saltos que puede tener
8.- Cuenta de saltos -8 bits
9.- Numero de secuencia de Mensaje
10.- Mensaje
-----------------------------------------------------------------------------"""
import struct
from Message_Hello import*
from Message_TC import*

class OLSR(Message_Hello,Message_TC):
    def __init__(self):
        self.Len_pq={
        'Hello':8,
        'TC':4
        }
        self.NSP=0
        self.TypeM={
        'Hello':b"",
        'TC':b""
        }
        self.Vtime=0
        self.Len_msj=0
        self.OAdd=b""
        self.TtoL=0
        self.HopC=0
        self.MSN=0
        self.msj=b""
        self.MHello=Message_Hello()
    def Empaquetado(self,Message_type):
        # Dependiendo el tipo de mensaje se manda a llamar a la funcion
        #Empacadora de mensaje Hello o Tc y regresa el mensaje empaquetado para
        # ser sumado al paquete ya hecho
        if Message_type=='Hello':
            Hello=self.MHello.Genera('WILL_LOW')
        elif Message_type=='TC':
            pass
        else:
            print("Error")
